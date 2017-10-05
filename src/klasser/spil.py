from klasser.spiller import *
from klasser.kortspil import *

class Spil:
	bruger = None
	aiSpillere = None
	kortspil = None
	spilErIGang = True

	def __init__(self, bruger, antalModstandere):
		self.bruger = bruger

		self.aiSpillere = [antalModstandere]


		for i in range(antalModstandere-1):
			self.aiSpillere[i] = AISpiller()

		self.kortspil = Kortspil()

		self.spilLøkke()
	
	def spilLøkke(self):
		while(self.spilErIGang):
			print(self.kortspil.nuværendeKort())
			print(self.kortspil.trækKort())
			self.spilErIGang = False