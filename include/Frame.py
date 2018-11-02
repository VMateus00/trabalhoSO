class Frame:

    pydCount = 0

    def __init__(self, process):
        self.pyd = Frame.pydCount
        Frame.pydCount += 1

        self.process = process
        self.executed = False
        self.offsetMemoria = None

        self.tempoExecutado = 0
