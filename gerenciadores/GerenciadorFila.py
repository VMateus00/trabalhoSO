from include.Frame import Frame


class GerenciadorFila:

    def __init__(self, listaProcessos):

        self.filaTempoReal = []
        self.filaProcessosUsuario = [[], [], []]

        self.filaProcessosProntos = [self.filaTempoReal, self.filaProcessosUsuario]

        for indice in range(len(listaProcessos)):

            if listaProcessos[indice].prioridadeProcesso == 0:
                self.filaTempoReal.append(Frame(listaProcessos[indice]))

            elif listaProcessos[indice].prioridadeProcesso == 1:
                self.filaProcessosUsuario[0].append(Frame(listaProcessos[indice]))

            elif listaProcessos[indice].prioridadeProcesso == 2:
                self.filaProcessosUsuario[1].append(Frame(listaProcessos[indice]))

            elif listaProcessos[indice].prioridadeProcesso == 3:
                self.filaProcessosUsuario[2].append(Frame(listaProcessos[indice]))

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
        # TODO
        pass
