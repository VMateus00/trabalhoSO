
# responsável pela criação de qualquer processo

self.tempoInicializacao = listaParametros[0]
        self.prioridadeProcesso = listaParametros[1]
        self.tempoProcessador = listaParametros[2]
        self.blocoMemoria  = listaParametros[3]
        self.codigoImpressora = listaParametros[4]
        self.requisicaoScanner = listaParametros[5]
        self.requisicaoModem = listaParametros[6]
        self.numeroCodigoDisco


def dispatcher():
    print("PID :", pid)
    print("Prioridade do processo:", prioridadeProcesso) 
    print("Offset da memória", offset_mem)
    print("Quantidade de blocos alocados", blocos_alocados)
    print("Utilização de impressora", impressora)
    print("Utilização de scanner", scanner)
    print("Utilização de drivers", drivers)

