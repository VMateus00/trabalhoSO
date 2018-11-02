class SistemaOperacional:
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
                instanteAtual +=1
        #         TODO executar acao

        # Terminou a execucao => chama o printer
        print(self.gerenciadorDisco.printMapaOcupacaoDoDisco())

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
        print("PID :", frame.pyd)
        print("Offset: ", frame.offsetMemoria)
        print("Prioridade do processo: ", frame.process.prioridadeProcesso)
        print("Time: ", frame.process.tempoProcessador)
        print("Utilização de impressora: ", frame.process.codigoImpressora)
        print("Utilização de scanner", frame.process.requisicaoScanner)
        print("Utilização de drivers: ", frame.process.codigoDisco)
        print()
