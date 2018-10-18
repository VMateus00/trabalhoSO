from include.MemBlock import MemBlock
from include.DiskOperation import DiskOperation

class File:

    def __init__(self, arquivo):
        self.tamanhoMemoria = arquivo.readline()
        self.segmentosOcupados = int(arquivo.readline())

        self.listaBlocos = []
        for i in range(self.segmentosOcupados):
            self.listaBlocos.append(self.readBloco(arquivo.readline()))

        self.listaOperacoes = []
        for line in arquivo:
            self.listaOperacoes.append(DiskOperation(line))

    def readBloco(self, line):
        line = line.split(',')
        return MemBlock(line)


