from include.DiskOperation import DiskOperation
from include.MemBlock import MemBlock


class GerenciadorDisco:
    def __init__(self, arquivo):
        self.tamanhoMemoria = int(arquivo.readline())
        segmentosOcupados = int(arquivo.readline())

        self.blocosOcupados = []
        for i in range(segmentosOcupados):
            self.blocosOcupados.append(self.readBloco(arquivo.readline()))

        self.listaOperacoes = []
        for line in arquivo:
            self.listaOperacoes.append(DiskOperation(line))

        self.blocosLivres = []
        self.carregaListaEspacosVazios()

    def readBloco(self, line):
        line = line.split(',')
        return MemBlock(line[0], line[1], line[2])

    def carregaListaEspacosVazios(self):
        blocoAtual = 0

        blocosOrdenadosPorPosicao = sorted(self.blocosOcupados, key=lambda block: block.posicaoInicial)

        for bloco in blocosOrdenadosPorPosicao:
            if blocoAtual < bloco.posicaoInicial:
                self.blocosLivres.append(MemBlock("livre", blocoAtual, bloco.posicaoInicial-blocoAtual))
                blocoAtual += bloco.posicaoInicial-blocoAtual
            blocoAtual += bloco.qtdBlocosOcupados

        if blocoAtual < self.tamanhoMemoria:
            self.blocosLivres.append(MemBlock("livre", blocoAtual, self.tamanhoMemoria-blocoAtual))

    def printMapaOcupacaoDoDisco(self):

        print("---------------------")
        print("|", end=""),

        posicaoArrayOcupado = 0
        posicaoArrayLivre = 0

        while posicaoArrayOcupado < len(self.blocosOcupados) or posicaoArrayLivre < len(self.blocosLivres):

            if posicaoArrayOcupado < len(self.blocosOcupados):
                blocoOcupadoAtual = self.blocosOcupados[posicaoArrayOcupado]
            else:
                blocoOcupadoAtual = MemBlock("99", 9999999, 0)

            if posicaoArrayLivre < len(self.blocosLivres):
                blocoLivreAtual = self.blocosLivres[posicaoArrayLivre]
            else:
                blocoLivreAtual = MemBlock("99", 9999999, 0)

            if blocoOcupadoAtual.posicaoInicial < blocoLivreAtual.posicaoInicial:
                i =0
                while i < blocoOcupadoAtual.qtdBlocosOcupados:
                    print(blocoOcupadoAtual.nome + "|", end="")
                    i +=1
                posicaoArrayOcupado +=1
            else:
                i = 0
                while i < blocoLivreAtual.qtdBlocosOcupados:
                    print("0|", end="")
                    i += 1
                posicaoArrayLivre += 1

        print("\n---------------------")
