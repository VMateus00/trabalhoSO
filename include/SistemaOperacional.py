class SistemaOperacional:

    QUANTUM = 1

    def __init__(self, gerenciadorProcessos, gerenciadorDisco, gerenciadorMemoria, gerenciadorEntradaSaida, gerenciadorFila):
        self.gerenciadorProcessos = gerenciadorProcessos
        self.gerenciadorDisco = gerenciadorDisco
        self.gerenciadorMemoria = gerenciadorMemoria
        self.gerenciadorEntradaSaida = gerenciadorEntradaSaida
        self.gerenciadorFila = gerenciadorFila

    def executaSO(self):
        instanteAtual = 0

        while not self.gerenciadorFila.isFilaProcessosVazia():
            frame = self.gerenciadorFila.getProcessoAtual(instanteAtual)
            if frame is None:
                instanteAtual += 1
            else:
                if self.gerenciadorProcessos.inicializaProcesso(self, frame):
                    self.dispatcherPrint(frame)

                if frame.executed:
                    instanteAtual = self.gerenciadorProcessos.executaProcesso(self, frame, instanteAtual)
                    self.gerenciadorDisco.executaOperacao(self)
                else:
                    self.gerenciadorFila.adicionaProcessoDeVoltaAListaDeProntos(frame)

        self.gerenciadorDisco.showDiskOperations(self)
        self.gerenciadorDisco.printMapaOcupacaoDoDisco()

    def dispatcherPrint(self, frame):
        print("Dispatcher => ")
        print("   PID :", frame.pid)
        print("   Offset: ", frame.offsetMemoria)
        print("   Prioridade do processo: ", frame.process.prioridadeProcesso)
        print("   Time: ", frame.process.tempoProcessador)
        print("   Utilização de impressora: ", frame.process.codigoImpressora)
        print("   Utilização de scanner", frame.process.requisicaoScanner)
        print("   Utilização de drivers: ", frame.process.codigoDisco)
        print()

    def liberaEspacoOcupadoProcesso(self, frame):
        self.gerenciadorMemoria.liberaProcessoDaMemoria(frame)

    def adicionaDadosEmMemoria(self, frame, isBlocoTempoReal):
        return self.gerenciadorMemoria.adicionaDadosEmMemoria(frame.process.blocoMemoria, isBlocoTempoReal)

    def verificaExisteFuncaoDiscoAExecutar(self, frame):
        return self.gerenciadorDisco.verificaExisteFuncaoDiscoAExecutar(frame)

    def obtemRecursosES(self, frame):
        return self.gerenciadorEntradaSaida.obtemRecursosES(frame)

    def liberaRecursosES(self, frame):
        self.gerenciadorEntradaSaida.liberaRecursos(frame)
        self.gerenciadorFila.verificaProcessoBloqueadoEAddNaFila(frame)

    def adicionaProcessoListaBloqueados(self, frame):
        self.gerenciadorFila.adicionaProcessoListaBloqueados(frame)

    def atualizaPrioridadeProcessos(self, instanteAtual):
        self.gerenciadorFila.atualizaPrioridadeProcessos(instanteAtual)

    def adicionaProcessoDeVoltaAListaDeProntos(self, frame):
        self.gerenciadorFila.adicionaProcessoDeVoltaAListaDeProntos(frame)

    def existsProcessWithCod(self, processCod):
        return self.gerenciadorProcessos.existsProcessWithCod(processCod)
