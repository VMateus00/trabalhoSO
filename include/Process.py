class Process:

    def __init__(self, parametros):
        listaParametros = parametros.split(',')
        self.tempoInicializacao = listaParametros[0]
        self.prioridadeProcesso = listaParametros[1]
        self.tempoProcessador = listaParametros[2]
        self.blocoMemoria  = listaParametros[3]
        self.codigoImpressora = listaParametros[4]
        self.requisicaoScanner = listaParametros[5]
        self.requisicaoModem = listaParametros[6]
        self.numeroCodigoDisco = listaParametros[7]



