class Process:

    def __init__(self, parametros):
        listaParametros = parametros.split(',')
        self.tempoInicializacao = int(listaParametros[0].strip())
        self.prioridadeProcesso = int(listaParametros[1].strip())
        self.tempoProcessador = int(listaParametros[2].strip())
        self.blocoMemoria = int(listaParametros[3].strip())
        self.codigoImpressora = int(listaParametros[4].strip())
        self.requisicaoScanner = int(listaParametros[5].strip())
        self.requisicaoModem = int(listaParametros[6].strip())
        self.codigoDisco = int(listaParametros[7].strip())



