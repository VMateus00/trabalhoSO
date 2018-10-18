from include.Process import Process

def main(arquivos):
    print("qualquer coisa")

    try:
        processos = arquivos[0]
        arquivoProcessos = open(processos, "r")

        operacoesArquivo = arquivos[1]
        arquivoOperacoes = open(operacoesArquivo, "r")

        listaProcessos = []
        for line in arquivoProcessos:
            listaProcessos.append(Process(line))

        Operacoes = File(arquivoOperacoes)


        print(listaProcessos)





    except:
        print("Não foi possivel pegar o nome dos arquivo")



if __name__=="__main__":
    main(arquivos=["processes.txt", "files.txt"])

