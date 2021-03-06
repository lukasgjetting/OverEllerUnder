import random
import konstanter

class Spiller:
	promille = 0
	navn = ""

	def __init__(self, navn):
		self.navn = navn;

	def hævPromille(self):
		"""Hæver brugerens promille med et tilfældigt kommatal mellem 0 og 2."""
		
		self.promille += random.random() * 2

	def erDød(self):
		"""Returnerer True hvis spillerens promille er over 4, ellers False."""
		
		if(self.promille >= 4):
			return True
		else:
			return False


class AISpiller(Spiller):

	def __init__(self):
		# Giver spilleren et tilfældigt navn.
		self.navn = konstanter.navne[random.randint(0, len(konstanter.navne)-1)]

	def gæt(self, nuværendeKort):
		"""
		Returnerer 0, 1 eller 2 alt efter om spilleren gætter på at næste kort er over, under eller lige på
		Spillerens nuværende promille påvirker dens logiske sans.
		"""

		# Gæt på at næste kort er over, hvis kortets værdi er tilstrækkeligt (i forhold til promillen) langt under 7.
		if(nuværendeKort.værdi + (self.promille * 2) < 7):
			return 0

		# Gæt på at næste kort er under, hvis kortets værdi er tilstrækkeligt (i forhold til promillen) langt over 7.
		elif(nuværendeKort.værdi - (self.promille * 2) > 7): 
			return 1
		
		# Ellers vælges muligheden tilfældigt, med en chance for at vælge lige på, der svarer til spillerens promille
		else:
			tilfældigt = random.randint(1, 100)

			# Hvis tallet er under brugerens promille ganget ti, tager brugeren den satsede beslutning! 
			if(tilfældigt < self.promille*10):
				return 2

			# Ellers vælges beslutningen bare efter om tallet er lige eller ulige.
			elif(tilfældigt % 2 == 0):
				return 0
			else:
				return 1