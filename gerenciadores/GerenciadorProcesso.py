from include.Frame import Frame
from include.SistemaOperacional import SistemaOperacional


class GerenciadorProcesso:
    def __init__(self, listaProcessos):
        self.processosProntos = listaProcessos
        self.listaFrames = []
        self.createFramesByProcessos(self.processosProntos)

    def createFramesByProcessos(self, processosProntos):
        for process in processosProntos:
            self.listaFrames.append(Frame(process))

    def getFrames(self):
        return self.listaFrames

    def existsProcessWithCod(self, processCod):
        return next(filter(lambda frame: frame.pidCount == processCod, self.listaFrames), None) is not None

    def inicializaProcesso(self, so, frame):
        if frame.executed is False:
            if so.gerenciadorEntradaSaida.obtemRecursosES(frame):
                isBlocoTempoReal = frame.process.prioridadeProcesso == 0
                offsetMemoria = so.gerenciadorMemoria.adicionaDadosEmMemoria(frame.process.blocoMemoria, isBlocoTempoReal)
                if offsetMemoria == -1:
                    print("Não há espaço em memoria para alocar o processo")
                    return False
                else:
                    frame.executed = True
                    return True
            else:
                so.gerenciadorFila.adicionaProcessoListaBloqueados(frame)
        else:
            return False

    def executaInstrucaoPorTempo(self, so, tempoExecucao, instrucaoAtual, pidProcess, isProcessTempoReal, instanteAtual):
        contadorTempo = 0
        while contadorTempo < tempoExecucao:
            print("P" + str(pidProcess) + " instruction " + str(instrucaoAtual+1))
            so.executaFuncaoDiscoSeExistir(pidProcess, isProcessTempoReal)
            so.gerenciadorFila.atualizaPrioridadeProcessos(instanteAtual)
            contadorTempo += 1
            instrucaoAtual += 1

        return instrucaoAtual

    def executaProcesso(self, so, frame, instanteAtual):
        if frame.process.prioridadeProcesso == 0:
            tempoTotalExecutado = 0
            while tempoTotalExecutado < frame.process.tempoProcessador:
                self.executaInstrucaoPorTempo(so, SistemaOperacional.QUANTUM, frame.instrucaoAtual, frame.pid, True, instanteAtual)
                tempoTotalExecutado += 1
            print("P" + str(frame.pid) + " return SIGINT")
            frame.tempoExecutado = frame.process.tempoProcessador
            so.liberaEspacoOcupadoProcesso(frame)
            so.liberaRecursosES(frame)
            return instanteAtual + frame.process.tempoProcessador
        else:
            frame.instrucaoAtual = so.executaInstrucaoPorTempo(so, SistemaOperacional.QUANTUM, frame.instrucaoAtual, frame.pid, False, instanteAtual)
            frame.tempoExecutado += SistemaOperacional.QUANTUM
            if frame.tempoExecutado == frame.process.tempoProcessador:
                print("P" + str(frame.pid) + " return SIGINT")
                so.liberaEspacoOcupadoProcesso(frame)
                so.liberaRecursosES(frame)
            else:
                so.gerenciadorFila.adicionaProcessoDeVoltaAListaDeProntos(frame)
            return instanteAtual+1
