class GerenciadorMemoria:
    def __init__(self):

        self.qtdMaximaBlocos = 1024
        self.qtdMaxBlocosProcessosTempoReal = 64
        self.qtdMaxBlocosProcessosUsuario = 960

        self.blocosUsadosProcTempoReal = 0
        self.blocosUsadosProcUsuario = 0

    def aumentaBlocosUtilizadosProcTempoReal(self, qtdBlocosAumentar):
        if((self.blocosUsadosProcTempoReal + qtdBlocosAumentar) > self.qtdMaxBlocosProcessosTempoReal):
            print("Error: o bloco não pode ser adicionado")
            # verificar o que fazer nesse caso

    def aumentaBlocosUtilizadosProcUsuario(self, qtdBlocosAumentar):
        if((self.blocosUsadosProcUsuario + qtdBlocosAumentar) > self.qtdMaxBlocosProcessosUsuario):
            print("Error: o bloco não pode ser adicionado")
            # verificar o que fazer nesse caso

    def adicionaDadosEmMemoria(self, qtdBlocosAdd, isBlocoTempoReal):
        if isBlocoTempoReal:
            if qtdBlocosAdd + self.blocosUsadosProcTempoReal > self.qtdMaxBlocosProcessosTempoReal:
                return -1
            else:
                retorno = self.blocosUsadosProcTempoReal
                self.blocosUsadosProcTempoReal += qtdBlocosAdd
                return retorno
        else:
            if qtdBlocosAdd + self.blocosUsadosProcUsuario > self.qtdMaxBlocosProcessosUsuario:
                return -1
            else:
                retorno = self.blocosUsadosProcUsuario
                self.blocosUsadosProcUsuario += qtdBlocosAdd
                return retorno
