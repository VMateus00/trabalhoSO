
# responsável pela criação de qualquer processo

# self.tempoInicializacao = listaParametros[0]
#        self.prioridadeProcesso = listaParametros[1]
#        self.tempoProcessador = listaParametros[2]
#        self.blocoMemoria  = listaParametros[3]
#        self.codigoImpressora = listaParametros[4]
#        self.requisicaoScanner = listaParametros[5]
#        self.requisicaoModem = listaParametros[6]
#        self.numeroCodigoDisco


def dispatcher(listaProcessos):
    for indice in range(len(listaProcessos)):
        print("PID :", indice)
        print("Prioridade do processo:", listaProcessos[indice].prioridade)
        if indice == 0: 
            print("Offset da memória: 0") # vamos mudar essa escrita pfvr, Henrique
        # else: calcular conforme o índice anterior
            print("Offset da memória:" )
        print("Quantidade de blocos alocados", listaProcessos[indice].blocoMemoria)
        if listaProcessos[indice].codigoImpressora == 0:
                print("Utilização de impressora: 0")
        else:
                print("Utilização de impressora: 1")    
        print("Utilização de scanner", listaProcessos[indice].requisicaoScaner)
        if listaProcessos[indice].codigoDisco == 0 or listaProcessos[indice].requisicaoModem == 0:
                print("Utilização de drivers: 0")
        else:
                print("Utilização de drivers: 1")

