class DiskOperation:
    def __init__(self, linhaArgumentos):
        linhaArgumentos = linhaArgumentos.split(',')

        self.processCod = linhaArgumentos[0]
        self.operationCod = linhaArgumentos[1]
        self.fileName = linhaArgumentos[2]
        if (len(linhaArgumentos) == 4):
            self.createOperation = linhaArgumentos[3]