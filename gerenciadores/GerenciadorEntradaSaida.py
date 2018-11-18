import threading


class GerenciadorEntradaSaida:

    def __init__(self):
        self.scanner = threading.Semaphore(1)
        self.impressora1 = threading.Semaphore(1)
        self.impressora2 = threading.Semaphore(1)
        self.modem = threading.Semaphore(1)
        self.dispositivosSATA1 = threading.Semaphore(1)
        self.dispositivosSATA2 = threading.Semaphore(1)

        self.dicioES = {
            "scanner": self.scanner,
            "impressora1": self.impressora1,
            "impressora2": self.impressora2,
            "modem": self.modem,
            "dispositivosSATA1": self.dispositivosSATA1,
            "dispositivosSATA2": self.dispositivosSATA2
        }

    # MÉTODOS DE PEGAR PERMISSÃO DOS DISPOSITIVOS

    def impressoraStatus(self, indice):
        return self.dicioES["impressora" + str(indice)].acquire(blocking=False)

    def scannerStatus(self):
        return self.dicioES["scanner"].acquire(blocking=False)

    def driverStatus(self, indice):
        return self.dicioES["dispositivosSATA" + str(indice)].acquire(blocking=False)

        # MÉTODOS DE DAR PERMISSÃO PRO DISPOSITIVO

    def impressoraRelease(self, indice):
        self.dicioES["impressora" + str(indice)].release()

    def scannerRelease(self):
        self.dicioES["scanner"].release()

    def driverRelease(self, indice):
        self.dicioES["dispositivosSATA" + str(indice)].release()

    def obtemRecursosES(self, frame):
        # Se o valor não quiser alguma impressora
        if frame.process.codigoImpressora == 0:
            impressoraBool = True

        # Caso queira alguma impressora
        else:
            impressoraBool = self.gerenciadorEntradaSaida.impressoraStatus(frame.process.codigoImpressora)

        # Se o processo não quiser o Scanner
        if frame.process.requisicaoScanner == 0:
            scannerBool = True

        # Caso queira o Scanner
        else:
            scannerBool = self.gerenciadorEntradaSaida.scannerStatus()

        # Caso o processo não quiser algum Dispositivo Sata
        if frame.process.codigoDisco == 0:
            driverBool = True

        # Caso o processor queira algum Dispositivo Sata
        else:
            driverBool = self.gerenciadorEntradaSaida.driverStatus(frame.process.codigoDisco)

        # Caso o processo consiga todos os seus dispositivos
        if impressoraBool is True and scannerBool is True and driverBool is True:
            return True

        # Caso o processo não consigo algum dos dispostivos
        else:
            # Devolve a permissão para a impressoraX caso a tenha pegado
            if impressoraBool is True and frame.process.codigoImpressora != 0:
                self.gerenciadorEntradaSaida.impressoraRelease(frame.process.codigoImpressora)

            # Devolve a permissão para o scanner caso o tenha pegado
            if scannerBool is True and frame.process.requisicaoScanner != 0:
                self.gerenciadorEntradaSaida.scannerRelease()

            # Devolve a permissão para o driverX caso o tenha pegado
            if driverBool is True and frame.process.codigoDisco != 0:
                self.gerenciadorEntradaSaida.driverRelease(frame.process.codigoDisco)

            return False
