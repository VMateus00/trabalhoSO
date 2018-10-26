from include.DiskOperation import DiskOperation
from include.MemBlock import MemBlock


class GerenciadorDisco:
    def __init__(self, arquivo):
        self.tamanhoMemoria = int(arquivo.readline())
        self.segmentosOcupados = int(arquivo.readline())

        self.listaBlocos = []
        for i in range(self.segmentosOcupados):
            self.listaBlocos.append(self.readBloco(arquivo.readline()))

        self.listaOperacoes = []
        for line in arquivo:
            self.listaOperacoes.append(DiskOperation(line))

        self.carregaListaEspacosVazios()

    def readBloco(self, line):
        line = line.split(',')
        return MemBlock(line[0], line[1], line[2])

    def carregaListaEspacosVazios(self):
        blocoAtual = 0

        self.blocosLivres = []
        self.blocosOrdenadosPorPosicao = sorted(self.listaBlocos, key=lambda block: block.posicaoInicial)

        for bloco in self.blocosOrdenadosPorPosicao:
            if blocoAtual < bloco.posicaoInicial:
                self.blocosLivres.append(MemBlock("livre", blocoAtual, bloco.posicaoInicial-blocoAtual))
                blocoAtual += bloco.posicaoInicial-blocoAtual
            blocoAtual += bloco.qtdBlocosOcupados

        if blocoAtual < self.tamanhoMemoria:
            self.blocosLivres.append(MemBlock("livre", blocoAtual, self.tamanhoMemoria-blocoAtual))
