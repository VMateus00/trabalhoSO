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
                instanteAtual += 1
            else:
                if self.inicializaProcesso(frame):
                    self.dispatcherPrint(frame)

                if frame.executed:
                    instanteAtual = self.executaProcesso(frame, instanteAtual)
                else:
                    self.gerenciadorFila.adicionaProcessoDeVoltaAListaDeProntos(frame)

        self.gerenciadorDisco.showDiskOperations()
        print(self.gerenciadorDisco.printMapaOcupacaoDoDisco())

    def executaProcesso(self, frame, instanteAtual):
        if frame.process.prioridadeProcesso == 0:
            self.executaInstrucaoPorTempo(frame.process.tempoProcessador, frame.instrucaoAtual, frame.pid, True)
            frame.tempoExecutado = frame.process.tempoProcessador
            print("P" + str(frame.pid) + " return SIGINT")
            self.liberaEspacoOcupadoProcesso(frame)
            return instanteAtual + frame.process.tempoProcessador
        else:
            frame.instrucaoAtual = self.executaInstrucaoPorTempo(SistemaOperacional.QUANTUM, frame.instrucaoAtual, frame.pid, False)
            frame.tempoExecutado += SistemaOperacional.QUANTUM
            if frame.tempoExecutado == frame.process.tempoProcessador:
                print("P" + str(frame.pid) + " return SIGINT")
                self.liberaEspacoOcupadoProcesso(frame)
            else:
                self.gerenciadorFila.adicionaProcessoDeVoltaAListaDeProntos(frame)
            return instanteAtual+1

    def executaInstrucaoPorTempo(self, tempoExecucao, instrucaoAtual, pidProcess, isProcessTempoReal):
        contadorTempo = 0
        while contadorTempo < tempoExecucao:
            print("P" + str(pidProcess) + " instruction " + str(instrucaoAtual+1))
            self.executaFuncaoDiscoSeExistir(pidProcess, isProcessTempoReal)
            contadorTempo += 1
            instrucaoAtual += 1

        return instrucaoAtual

    def inicializaProcesso(self, frame):
        if frame.executed is False:
            if self.obtemRecursosES(frame):
                isBlocoTempoReal = frame.process.prioridadeProcesso == 0
                offsetMemoria = self.gerenciadorMemoria.adicionaDadosEmMemoria(frame.process.blocoMemoria,
                                                                               isBlocoTempoReal)
                if offsetMemoria == -1:
                    print("Não há espaço em memoria para alocar o processo")
                    return False
                else:
                    frame.executed = True
                    return True
        else:
            return False

    def obtemRecursosES(self, frame):
        # Se o valor não quiser alguma impressora
        if frame.process.codigoImpressora == 0:
            impressoraBool = True

        # Caso queira alguma impressora
        else:
            impressoraBool = self.gerenciadorEntradaSaida.impressoraStatus(frame.process.codigoImpressora)

        # Se o processo não quiser o Scanner
        if frame.process.requisicaoScanner == 0:
            scannerBool = True

        # Caso queira o Scanner
        else:
            scannerBool = self.gerenciadorEntradaSaida.scannerStatus()

        # Caso o processo não quiser algum Dispositivo Sata
        if frame.process.codigoDisco == 0:
            driverBool = True

        # Caso o processor queira algum Dispositivo Sata
        else:
            driverBool = self.gerenciadorEntradaSaida.driverStatus(frame.process.codigoDisco)

        # Caso o processo consiga todos os seus dispositivos
        if impressoraBool is True and scannerBool is True and driverBool is True:
            return True

        # Caso o processo não consigo algum dos dispostivos
        else:
            # Devolve a permissão para a impressoraX caso a tenha pegado
            if impressoraBool is True and frame.process.codigoImpressora != 0:
                self.gerenciadorEntradaSaida.impressoraRelease(frame.process.codigoImpressora)

            # Devolve a permissão para o scanner caso o tenha pegado
            if scannerBool is True and frame.process.requisicaoScanner != 0:
                self.gerenciadorEntradaSaida.scannerRelease()

            # Devolve a permissão para o driverX caso o tenha pegado
            if driverBool is True and frame.process.codigoDisco != 0:
                self.gerenciadorEntradaSaida.driverRelease(frame.process.codigoDisco)

            return False

    def dispatcherPrint(self, frame):
        print()
        print("PID :", frame.pid)
        print("Offset: ", frame.offsetMemoria)
        print("Prioridade do processo: ", frame.process.prioridadeProcesso)
        print("Time: ", frame.process.tempoProcessador)
        print("Utilização de impressora: ", frame.process.codigoImpressora)
        print("Utilização de scanner", frame.process.requisicaoScanner)
        print("Utilização de drivers: ", frame.process.codigoDisco)
        print()

    def liberaEspacoOcupadoProcesso(self, frame):
        self.gerenciadorMemoria.liberaProcessoDaMemoria(frame)

    def executaFuncaoDiscoSeExistir(self, pidProcess, isProcessTempoReal):
        self.gerenciadorDisco.executaFuncaoDiscoSeExistir(pidProcess, isProcessTempoReal)
