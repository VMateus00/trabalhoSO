class Process:

    def __init__(self, parametros):
        listaParametros = parametros.split(',')
        self.tempoInicializacao = int(listaParametros[0])
        self.prioridadeProcesso = int(listaParametros[1])
        self.tempoProcessador = int(listaParametros[2])
        self.blocoMemoria = int(listaParametros[3])
        self.codigoImpressora = int(listaParametros[4])
        self.requisicaoScanner = int(listaParametros[5])
        self.requisicaoModem = int(listaParametros[6])
        self.codigoDisco = int(listaParametros[7])



