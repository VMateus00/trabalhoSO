import time

class SistemaOperacional:

    QUANTUM = 1

    def __init__(self, gerenciadorProcessos, gerenciadorDisco, gerenciadorMemoria, gerenciadorEntradaSaida, gerenciadorFila):
        self.gerenciadorProcessos = gerenciadorProcessos
        self.gerenciadorDisco = gerenciadorDisco
        self.gerenciadorMemoria = gerenciadorMemoria
        self.gerenciadorEntradaSaida = gerenciadorEntradaSaida
        self.gerenciadorFila = gerenciadorFila

        instanteAtual = 0

        while not self.gerenciadorFila.isFilaProcessosVazia():
            frame = self.gerenciadorFila.getProcessoAtual(instanteAtual)
            if frame is None:
                instanteAtual +=1
            else:
                if self.inicializaProcesso(frame):
                    self.dispatcherPrint(frame)
                instanteAtual = self.executaProcesso(frame, instanteAtual)

        print(self.gerenciadorDisco.printMapaOcupacaoDoDisco())

    def executaProcesso(self, frame, instanteAtual):
        if frame.process.prioridadeProcesso == 0:
            self.executaInstrucaoPorTempo(frame.process.tempoProcessador, frame.instrucaoAtual, frame.pid)
            print("P" + str(frame.pid) + " return SIGINT")
            return instanteAtual + frame.process.tempoProcessador
        else:
            frame.instrucaoAtual = self.executaInstrucaoPorTempo(SistemaOperacional.QUANTUM, frame.instrucaoAtual, frame.pid)
            frame.tempoExecutado += SistemaOperacional.QUANTUM
            if frame.tempoExecutado == frame.process.tempoProcessador:
                print("P" + str(frame.pid) + " return SIGINT")
                self.liberaEspacoOcupadoProcesso(frame)
            else:
                self.gerenciadorFila.adicionaProcessoDevoltaALista(frame)
            return instanteAtual+1

    def executaInstrucaoPorTempo(self, tempoExecucao, instrucaoAtual, pidProcess):
        tempoAtual = time.time()
        tempoExecutado = time.time()

        while(tempoExecutado - tempoAtual) <= tempoExecucao:
            print("P" + str(pidProcess) + " instruction " + str(instrucaoAtual))
            instrucaoAtual +=1
            tempoExecutado = time.time()
        return instrucaoAtual

    def inicializaProcesso(self, frame):
        if frame.executed is False:
            frame.executed = True

            isBlocoTempoReal = frame.process.prioridadeProcesso == 0
            offsetMemoria = self.gerenciadorMemoria.adicionaDadosEmMemoria(frame.process.blocoMemoria, isBlocoTempoReal)
            if offsetMemoria == -1:
                print("Não há espaço em memoria para alocar o processo")
                return False
            else:
                frame.offsetMemoria = offsetMemoria
                return self.obtemRecursosDisco(frame)
        else:
            return True

    def obtemRecursosDisco(self, frame):
        return True

    def dispatcherPrint(self, frame):
        print("PID :", frame.pid)
        print("Offset: ", frame.offsetMemoria)
        print("Prioridade do processo: ", frame.process.prioridadeProcesso)
        print("Time: ", frame.process.tempoProcessador)
        print("Utilização de impressora: ", frame.process.codigoImpressora)
        print("Utilização de scanner", frame.process.requisicaoScanner)
        print("Utilização de drivers: ", frame.process.codigoDisco)
        print()

    def liberaEspacoOcupadoProcesso(self, frame):
        # TODO
        pass
