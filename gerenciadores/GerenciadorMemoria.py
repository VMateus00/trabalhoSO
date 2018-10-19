from include.DiskOperation import DiskOperation
from include.MemBlock import MemBlock


class GerenciadorMemoria:
    def __init__(self, arquivo):
        self.tamanhoMemoria = arquivo.readline()
        self.segmentosOcupados = int(arquivo.readline())

        self.listaBlocos = []
        for i in range(self.segmentosOcupados):
            self.listaBlocos.append(self.readBloco(arquivo.readline()))

        self.listaOperacoes = []
        for line in arquivo:
            self.listaOperacoes.append(DiskOperation(line))
        # TODO criar lista com os blocos vazios a partir da lista de blocos utilizados

    def readBloco(self, line):
        line = line.split(',')
        return MemBlock(line)