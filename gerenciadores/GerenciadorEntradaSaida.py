import threading


class GerenciadorEntradaSaida:

    def __init__(self):
<<<<<<< HEAD
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

	# MÉTODOS DE PEGAR PERMISSÃO DOS DISPOSITIVOS

	def  impressoraStatus(self, indice):
		
		return self.dicioES["impressora" + str(indice)].acquire(blocking=False)

	def  scannerStatus(self):
		
		return self.dicioES["scanner"].acquire(blocking=False)

	def  driverStatus(self, indice):
		
		return self.dicioES["dispositivosSATA" + str(indice)].acquire(blocking=False)

	# MÉTODOS DE DAR PERMISSÃO PRO DISPOSITIVO

	def impressoraRelease(self, indice):

		self.dicioES["impressora" + str(indice)].release()

	def scannerRelease(self):

		self.dicioES["scanner"].release()

	def driverRelease(self, indice):

=======
>>>>>>> ef48405f2bafe8fa548fdf923d51c5e6775fd12d
