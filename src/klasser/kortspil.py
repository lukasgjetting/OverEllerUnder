import random
import konstanter

class Kortspil:
	kort = None

	def __init__(self):
		self.kort = []

		self.bland()

	def bland(self):
		'''Tilføjer et af hvert kort til listen self.kort og blander derefter disse i tilfældig rækkefølge.'''
		
		for værdi in range(1, 14):
			for kulør in range(4):
				self.kort.append(Kort(værdi, kulør))

		random.shuffle(self.kort)

	def nuværendeKort(self):
		return self.kort[len(self.kort)-1]

	def trækOgSammenlignKort(self):
		'''Fjerner et kort fra kortspillet og returnerer 0 hvis det nye er over, 1 hvis det er under og 2 hvis det er lige på.'''

		# Gem det nuværende kort og fjern det derefter fra listen
		før = self.nuværendeKort()
		self.kort.pop()

		# Hvis der ikke er flere kort tilbage, blander vi kortene og begynder forfra.
		if(len(self.kort) == 0):
			self.bland()
		
		# Returner den rigtige værdi
		if(self.nuværendeKort().værdi > før.værdi):
			return 0
		elif(self.nuværendeKort().værdi < før.værdi):
			return 1
		else:
			return 2



class Kort:

	værdi = 0
	kulør = 0

	def __init__(self, værdi, kulør):
		self.værdi = værdi
		self.kulør = kulør
		
	def tilStreng(self):
		'''Konverterer kortet til en streng, der kan skrives til konsollen.'''
		
		return konstanter.kortKulørTekst[self.kulør] + " " + konstanter.kortVærdiTekst[self.værdi]