from gerenciadores.GerenciadorMemoria import GerenciadorMemoria
from include.Process import Process

def main(arquivos):
    try:
        processos = arquivos[0]
        arquivoProcessos = open(processos, "r")

        operacoesArquivo = arquivos[1]
        arquivoOperacoes = open(operacoesArquivo, "r")

        listaProcessos = []
        for line in arquivoProcessos:
            listaProcessos.append(Process(line))

        gerenciadorMemoria = GerenciadorMemoria(arquivoOperacoes);


        print(listaProcessos)

    except:
        print("Não foi possivel pegar o nome dos arquivo")
#         remover essa exception geral e criar uma especifica para cada parte



if __name__=="__main__":
    main(arquivos=["processes.txt", "files.txt"])

