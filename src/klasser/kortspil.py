import random

class Kortspil:
	kort = None

	def __init__(self):
		self.kort = []

		for værdi in range(1, 14):
			for kulør in range(4):
				self.kort.append(Kort(værdi, kulør))

		random.shuffle(self.kort)

	def nuværendeKort(self):
		return self.kort[len(self.kort)-1]

	def trækKort(self):
		# Fjerner et kort fra kortspillet og returnerer 0 hvis det nye er over, 1 hvis det er under og 2 hvis det er lige på.
		før = self.nuværendeKort()
		self.kort.pop()
		
		if(self.nuværendeKort().værdi > før.værdi):
			return 0
		elif(self.nuværendeKort().værdi < før.værdi) :
			return 1
		else:
			return 2

kortVærdiTekst = {
	1: "Es",
	2: "To",
	3: "Tre",
	4: "Fire",
	5: "Fem",
	6: "Seks",
	7: "Syv",
	8: "Otte",
	9: "Ni",
	10: "Ti",
	11: "Bonde",
	12: "Dame",
	13: "Konge"
}

kortKulørTekst = {
	0: "Hjerter",
	1: "Ruder",
	2: "Spar",
	3: "Klør"
}

class Kort:

	værdi = 0
	kulør = 0

	def __init__(self, værdi, kulør):
		self.værdi = værdi
		self.kulør = kulør
		
	def tilStreng(self):
		return kortKulørTekst[self.kulør] + " " + kortVærdiTekst[self.værdi]