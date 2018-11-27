class GerenciadorFila:

    def __init__(self, listaFrames):

        self.filaTempoReal = []
        self.filaProcessosUsuario = [[], [], []]

        self.filaProcessosProntos = [self.filaTempoReal, self.filaProcessosUsuario]
        self.filaProcessosBloqueados = []

        for frame in listaFrames:
            if frame.process.prioridadeProcesso == 0:
                self.filaTempoReal.append(frame)
            elif frame.process.prioridadeProcesso == 1:
                self.filaProcessosUsuario[0].append(frame)
            elif frame.process.prioridadeProcesso == 2:
                self.filaProcessosUsuario[1].append(frame)
            elif frame.process.prioridadeProcesso == 3:
                self.filaProcessosUsuario[2].append(frame)
            else:
                print("Prioridade inconsistente")

        self.filaTempoReal.sort(key=lambda frame: frame.process.tempoInicializacao)
        self.filaProcessosUsuario[0].sort(key=lambda frame: frame.process.tempoInicializacao)
        self.filaProcessosUsuario[1].sort(key=lambda frame: frame.process.tempoInicializacao)
        self.filaProcessosUsuario[2].sort(key=lambda frame: frame.process.tempoInicializacao)

    def getProcessoAtual(self, instanteAtual):
        #Verifica se há processos na fila de tempo real (prioridade 0).
        # if not self.filaProcessosProntos[0]:
        if len(self.filaProcessosProntos[0]) != 0:
            #Procura o primeiro processo na fila que tenha o tempo de incialização menor ou igual ao instante atual
            for indice in range(len(self.filaTempoReal)):
                if self.filaTempoReal[indice].process.tempoInicializacao <= instanteAtual:
                    return self.filaTempoReal.pop(indice)

        #Verifica se há processos na fila de processos usuário.
        if len(self.filaProcessosProntos[1]) != 0:
            #Verifica se há processos na fila de prioridade 1.
            if len(self.filaProcessosUsuario[0]) != 0:
                #Procura o primeiro processo na fila que tenha o tempo de incialização menor ou igual ao instante atual
                for indice in range(len(self.filaProcessosUsuario[0])):
                    if self.filaProcessosUsuario[0][indice].process.tempoInicializacao <= instanteAtual:
                        return self.filaProcessosUsuario[0].pop(indice)

            #Verifica se há processos na fila de prioridade 2.
            if len(self.filaProcessosUsuario[1]) != 0:
                #Procura o primeiro processo na fila que tenha o tempo de incialização menor ou igual ao instante atual
                for indice in range(len(self.filaProcessosUsuario[1])):
                    if self.filaProcessosUsuario[1][indice].process.tempoInicializacao <= instanteAtual:
                        return self.filaProcessosUsuario[1].pop(indice)

            #Verifica se há processos na fila de prioridade 3.
            if len(self.filaProcessosUsuario[2]) != 0:
                #Procura o primeiro processo na fila que tenha o tempo de incialização menor ou igual ao instante atual
                for indice in range(len(self.filaProcessosUsuario[2])):
                    if self.filaProcessosUsuario[2][indice].process.tempoInicializacao <= instanteAtual:
                        return self.filaProcessosUsuario[2].pop(indice)
        return None

    def isFilaProcessosVazia(self):
        if len(self.filaTempoReal) == 0 and len(self.filaProcessosUsuario[0]) == 0 \
                and len(self.filaProcessosUsuario[1]) == 0 and len(self.filaProcessosUsuario[1]) == 0:
            return True
        else:
            return False

    def adicionaProcessoDeVoltaAListaDeProntos(self, frame):
        if frame.motivoBloqueado == 0:
            if frame.tempoExecutado < frame.process.tempoProcessador:
                if frame.process.prioridadeProcesso == 0:
                    self.filaTempoReal.append(frame)
                else:
                    self.filaProcessosUsuario[frame.process.prioridadeProcesso-1].append(frame)

            if self.filaProcessosBloqueados.count(frame):
                self.filaProcessosBloqueados.remove(frame)
            frame.quantumEsperando = 0

    def atualizaPrioridadeProcessos(self, instanteAtual):
        # Para cada processo, aumentar o contador de prioridade dele em 1 quantum
        # quando completa 10 quantuns na fila de prioridade, ele passa pra uma prioridade acima

        framesParaPrioridadeUm = []
        framesParaPrioridadeDois = []

        # Atualizando fila de prioridade 2
        for frame in filter(lambda frame: frame.process is not None and frame.process.tempoInicializacao < instanteAtual, self.filaProcessosUsuario[1]):
            if frame.quantumEsperando == 10:
                frame.quantumEsperando = 0
                framesParaPrioridadeUm.append(frame)
            else:
                frame.quantumEsperando +=1

        # Atualizando fila de prioridade 3
        for frame in filter(lambda frame: frame.process.tempoInicializacao < instanteAtual, self.filaProcessosUsuario[2]):
            if frame.quantumEsperando == 10:
                frame.quantumEsperando = 0
                framesParaPrioridadeDois.append(frame)
            else:
                frame.quantumEsperando +=1

        # Remove frames da lista de prioridade 2
        for frameToRemove in framesParaPrioridadeUm:
            self.filaProcessosUsuario[1].remove(frameToRemove)

        # Remove frames da lista de prioridade 3
        for frameToRemove in framesParaPrioridadeDois:
            self.filaProcessosUsuario[2].remove(frameToRemove)

        # Adiciona na nova fila de prioridade
        self.filaProcessosUsuario[0] += framesParaPrioridadeUm
        self.filaProcessosUsuario[1] += framesParaPrioridadeDois

    def adicionaProcessoListaBloqueados(self, frame):
        self.filaProcessosBloqueados.append(frame)

    def verificaProcessoBloqueadoEAddNaFila(self, frame):
        # Trazer processos que foram bloqueados por recurso de E/S não olhar os bloqueados por disco
        for frameEncontrado in filter(lambda frame : frame.motivoBloqueado == 2, self.filaProcessosBloqueados):

            liberaScanner = frameEncontrado.process.requisicaoScanner == 0 or (frame.process.requisicaoScanner != 0
                                                                             and frameEncontrado.process.requisicaoScanner == frame.process.requisicaoScanner)

            liberaModem = frameEncontrado.process.requisicaoModem == 0 or (frame.process.requisicaoModem != 0
                                                                           and frameEncontrado.process.requisicaoModem == frame.process.requisicaoModem)

            liberaImpressora = frameEncontrado.process.codigoImpressora == 0 or (frame.process.codigoImpressora != 0
                                                                                 and frameEncontrado.process.codigoImpressora == frame.process.codigoImpressora)
            if liberaScanner and liberaModem and liberaImpressora:
                self.filaProcessosBloqueados.remove(frameEncontrado)
                frameEncontrado.motivoBloqueado = 0
                if frameEncontrado.process.prioridadeProcesso == 0:
                    self.filaTempoReal.append(frameEncontrado)
                else:
                    self.filaProcessosUsuario[frameEncontrado.process.prioridadeProcesso-1].append(frameEncontrado)
