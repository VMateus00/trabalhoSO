class Frame:

    pidCount = 0

    def __init__(self, process):
        self.pid = Frame.pidCount
        Frame.pidCount += 1

        self.process = process
        self.executed = False
        self.offsetMemoria = None
        self.tempoExecutado = 1
        self.instrucaoAtual = 0
        self.quantumEsperando = 0

        self.motivoBloqueado = 0

        # lista de motivos para bloqueio
        # 0 - nao está bloqueado
        # 1 - bloqueado por operacao de disco
        # 2 - bloqueado por recurso nao obtido
        # 3 - bloqueado por nao conseguir memoria
