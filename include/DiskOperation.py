class DiskOperation:
    def __init__(self, linhaArgumentos):
        linhaArgumentos = linhaArgumentos.split(',')

        self.processCod = int(linhaArgumentos[0].strip())
        self.operationCod = int(linhaArgumentos[1].strip())
        self.fileName = linhaArgumentos[2].strip()
        if (len(linhaArgumentos) == 4):
            self.createOperation = int(linhaArgumentos[3].strip())