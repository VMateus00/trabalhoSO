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
                self.dispatcher(frame);
                instanteAtual +=1
        #         TODO executar acao

        # Terminou a execucao => chama o printer
        print(self.gerenciadorDisco.printMapaOcupacaoDoDisco())

    def dispatcher(self, frame):
        print("PID :", frame.pyd)
        print("Offset: ", frame.offsetMemoria)
        print("Prioridade do processo: ", frame.process.prioridadeProcesso)
        print("Time: ", frame.process.tempoProcessador)
        print("Utilização de impressora: ", frame.process.codigoImpressora)
        print("Utilização de scanner", frame.process.requisicaoScanner)
        print("Utilização de drivers: ", frame.process.codigoDisco)
        print()
