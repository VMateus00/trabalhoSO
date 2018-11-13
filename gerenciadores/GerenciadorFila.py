class GerenciadorFila:

    def __init__(self, listaFrames):

        self.filaTempoReal = []
        self.filaProcessosUsuario = [[], [], []]

        self.filaProcessosProntos = [self.filaTempoReal, self.filaProcessosUsuario]

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
        if len(self.filaProcessosProntos[0]) != 0 and self.filaTempoReal[0].process.tempoInicializacao <= instanteAtual:
            return self.filaTempoReal.pop(0)
        elif len(self.filaProcessosProntos[1]) != 0:
            if len(self.filaProcessosUsuario[0]) != 0 and self.filaProcessosUsuario[0][0].process.tempoInicializacao <= instanteAtual:
                    return self.filaProcessosUsuario[0].pop(0)
            elif len(self.filaProcessosUsuario[1]) != 0 and self.filaProcessosUsuario[1][0].process.tempoInicializacao <= instanteAtual:
                    return self.filaProcessosUsuario[1].pop(0)
            elif len(self.filaProcessosUsuario[2]) != 0 and self.filaProcessosUsuario[2][0].process.tempoInicializacao <= instanteAtual:
                    return self.filaProcessosUsuario[2].pop(0)
        return None

    def isFilaProcessosVazia(self):
        if len(self.filaTempoReal) == 0 and len(self.filaProcessosUsuario[0]) == 0 \
                and len(self.filaProcessosUsuario[1]) == 0 and len(self.filaProcessosUsuario[1]) == 0:
            return True
        else:
            return False

    def adicionaProcessoDeVoltaAListaDeProntos(self, frame):
        if frame.tempoExecutado < frame.process.tempoProcessador:
            self.filaProcessosUsuario[frame.process.prioridadeProcesso-1].append(frame)
            frame.quantumEsperando = 0

    def atualizaPrioridadeProcessos(self, instanteAtual):
        # Para cada processo, aumentar o contador de prioridade dele em 1 ponto
        # quando completa 10 quantuns na fila de prioridade, ele passa pra uma prioridade acima

        framesParaPrioridadeUm = []
        framesParaPrioridadeDois = []

        for frame in filter(lambda frame: frame.process is not None and frame.process.tempoInicializacao < instanteAtual, self.filaProcessosUsuario[1]):
            if frame.quantumEsperando == 10:
                framesParaPrioridadeUm.append(frame)
            else:
                frame.quantumEsperando +=1

        for frame in filter(lambda frame: frame.process.tempoInicializacao < instanteAtual, self.filaProcessosUsuario[2]):
            if frame.quantumEsperando == 10:
                framesParaPrioridadeDois.append(frame)
            else:
                frame.quantumEsperando +=1

        for frameToRemove in framesParaPrioridadeUm:
            self.filaProcessosUsuario[1].remove(frameToRemove)

        for frameToRemove in framesParaPrioridadeDois:
            self.filaProcessosUsuario[2].remove(frameToRemove)

        self.filaProcessosUsuario[0] += framesParaPrioridadeUm
        self.filaProcessosUsuario[1] += framesParaPrioridadeDois
