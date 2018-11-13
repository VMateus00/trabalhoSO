from include.Frame import Frame


class GerenciadorProcesso:
    def __init__(self, listaProcessos):
        self.processosProntos = listaProcessos
        self.listaFrames = []
        self.createFramesByProcessos(self.processosProntos)

    def createFramesByProcessos(self, processosProntos):
        for process in processosProntos:
            self.listaFrames.append(Frame(process))

    def getFrames(self):
        return self.listaFrames

    def existsProcessWithCod(self, processCod):
        return next(filter(lambda frame: frame.pidCount == processCod, self.listaFrames), None) is not None

