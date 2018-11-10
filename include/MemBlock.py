class MemBlock:

    def __init__(self, nome, posicaoInicial, qtdBlocosOcupados):
        self.nome = nome
        self.posicaoInicial = int(posicaoInicial)
        self.qtdBlocosOcupados = int(qtdBlocosOcupados)
        self.processoCriouCod = -1  # variavel para garantir que processos de usuarios diferentes não possam deletar arquivos de outros processos
