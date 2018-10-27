import threading


class GerenciadorEntradaSaida:

    def __init__(self):
        self.scanner = threading.Semaphore(1)
        self.impressoras = threading.Semaphore(2)
        self.modem = threading.Semaphore(1)
        self.dispositivosSATA = threading.Semaphore(2)

