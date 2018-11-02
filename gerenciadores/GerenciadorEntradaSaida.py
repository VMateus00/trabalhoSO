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
	        "scanner" : self.scanner,
	        "impressora1" : self.impressora1,
	        "impressora2" : self.impressora2,
	        "modem" : self.modem,
	        "dispositivosSATA1" : self.dispositivosSATA1,
	        "dispositivosSATA2" : self.dispositivosSATA2
		}