class GerenciadorFila:

	def __init__(self, listaProcessos):
		self.filaProcessosProntos = []

		self.filaTempoReal = []
		self.filaProcessosUsuario = [[], [], []]

		for indice in range(len(listaProcessos)):
			if (listaProcessos[indice].prioridade == "0"):
				self.filaTempoReal.append(listaProcessos[indice])
			elif (listaProcessos[indice].prioridade == 1):
				self.filaProcessosUsuario[1].append(listaProcessos[indice])
			elif (listaProcessos[indice].prioridade == 2):
				self.filaProcessosUsuario[2].append(listaProcessos[indice])
			elif (listaProcessos[indice].prioridade == 3):
				self.filaProcessosUsuario[3].append(listaProcessos[indice])
			else:
				print("Prioridade inconsistente")

