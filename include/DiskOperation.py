class DiskOperation:
    def __init__(self, linhaArgumentos, identificadorOperacao):
        linhaArgumentos = linhaArgumentos.split(',')

        self.isExecuted = False
        self.operationCod = identificadorOperacao
        self.processCod = int(linhaArgumentos[0].strip())
        self.typeOfOperation = int(linhaArgumentos[1].strip())
        self.fileName = linhaArgumentos[2].strip()
        if len(linhaArgumentos) == 4:
            self.createOperation = int(linhaArgumentos[3].strip())

        self.msgSaida = ""
