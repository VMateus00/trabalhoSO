from gerenciadores.GerenciadorDisco import GerenciadorDisco
from gerenciadores.GerenciadorEntradaSaida import GerenciadorEntradaSaida
from gerenciadores.GerenciadorMemoria import GerenciadorMemoria
from gerenciadores.GerenciadorProcesso import GerenciadorProcesso
from gerenciadores.GerenciadorFila import GerenciadorFila
from include.Process import Process
from include.SistemaOperacional import SistemaOperacional


def main(arquivos):
    try:
        processos = arquivos[0]
        arquivoProcessos = open(processos, "r")

        operacoesArquivo = arquivos[1]
        arquivoOperacoes = open(operacoesArquivo, "r")

    except:
        print("Não foi possivel pegar o nome dos arquivo")
#         remover essa exception geral e criar uma especifica para cada parte

    listaProcessos = []

    contadorQtdProcessos=0
    for line in arquivoProcessos:
        listaProcessos.append(Process(line))
        contadorQtdProcessos += 1
        if contadorQtdProcessos == 999:
            print("Foi atingido o maximo de processos suportados, os seguintes serão ignorados!")
            break

    gerenciadorProcessos = GerenciadorProcesso(listaProcessos)
    gerenciadorDisco = GerenciadorDisco(arquivoOperacoes)
    gerenciadorMemoria = GerenciadorMemoria()
    gerenciadorEntradaSaida = GerenciadorEntradaSaida()
    gerenciadorFila = GerenciadorFila(gerenciadorProcessos.getFrames())

    so = SistemaOperacional(gerenciadorProcessos, gerenciadorDisco, gerenciadorMemoria, gerenciadorEntradaSaida, gerenciadorFila)
    so.executaSO()

if __name__=="__main__":
    main(arquivos=["processes.txt", "files.txt"])

