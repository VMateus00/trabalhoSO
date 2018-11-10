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
        identificadorOperacao = 0
        for line in arquivo:
            self.listaOperacoes.append(DiskOperation(line, identificadorOperacao))
            identificadorOperacao += 1

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

    def executaFuncaoDiscoSeExistir(self, pidProcess, isProcessTempoReal):
        self.listaOperacoes.sort(key=lambda diskOperation : diskOperation.operationCod)
        for diskOperation in filter(lambda diskOperation: diskOperation.processCod == pidProcess, self.listaOperacoes):
            if not diskOperation.isExecuted:
                diskOperation.isExecuted = True
                self.executaOperacao(diskOperation, pidProcess, isProcessTempoReal)
                break

    # TODO ainda incompleto
    def executaOperacao(self, diskOperation, pidProcess, isProcessTempoReal):
        if diskOperation.typeOfOperation == 0:  # O => cria arquivos em disco
            bloco = self.getBlocoMemoriaLivreSeExistir(diskOperation.createOperation)
            if bloco is None:
                diskOperation.msgSaida = "O processo " + str(pidProcess) + " não pode criar o arquivo " + diskOperation.fileName + " (Falta de espaço)."
            else:
                bloco.processoCriouCod = pidProcess
            print()
        elif diskOperation.typeOfOperation == 1:  # 1 => remove arquivos em disco
            print()
        else:
            diskOperation.msgSaida = "Operação inválida"

    def getBlocoMemoriaLivreSeExistir(self, qtdBlocosNecessarios):

        bloco = self.getFirstBlocoLivre(qtdBlocosNecessarios)
        if bloco is None:
            return None
        else:
            # criar um bloco do tamanho exato se for maior, liberando o espaco que nao foi usado
            if bloco.qtdBlocosOcupados > qtdBlocosNecessarios:
                posicaoInicialNovoBlocoVazio = bloco.posicaoInicial + (bloco.qtdBlocosOcupados - qtdBlocosNecessarios)
                qtdBlocosOcupados = bloco.qtdBlocosOcupados - qtdBlocosNecessarios
                self.blocosLivres.append(MemBlock("livre", posicaoInicialNovoBlocoVazio, qtdBlocosOcupados))
                self.blocosLivres.sort(key=lambda bloco : bloco.posicaoInicial)
        self.blocosOcupados.append(bloco)
        self.blocosOcupados.sort(key=lambda bloco : bloco.posicaoInicial)

        return bloco

    def getFirstBlocoLivre(self, qtdBlocos):
        # TODO remover esse for e colocar um utilitario padrao da linguagem
        for bloco in self.blocosLivres:
            if bloco.qtdBlocosOcupados >= qtdBlocos:
                # TODO fazer com que ele remova esse bloco da lista de blocos livres
                return bloco
        return None

    # Metodo para mostrar as operacoes de disco elas só aparecem ao terminar os processos,
    # apesar de serem feitas enquanto executa
    def showDiskOperations(self):
        print("Sistema de arquivos => ")
        for diskOperation in self.listaOperacoes:
            print("Operação " + diskOperation.operationCod + " => ", end="")
            if diskOperation.resultadoOperacao:
                print("Sucesso")
            else:
                print("Falha")

            print(diskOperation.msgSaida)
