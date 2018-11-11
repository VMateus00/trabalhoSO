class Frame:

    pidCount = 0

    def __init__(self, process):
        self.pid = Frame.pidCount
        Frame.pidCount += 1

        self.process = process
        self.executed = False
        self.offsetMemoria = None
        self.tempoExecutado = 0
        self.instrucaoAtual = 0
        self.quantumEsperando = 0
