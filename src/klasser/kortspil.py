import random

class Kortspil:
	kort = None

	def __init__(self):
		kort = []

		for værdi in range(1, 14):
			for kulør in range(4):
				kort.append(Kort(værdi, kulør))

		random.shuffle(kort)

		for i in range(len(kort)):
			print(kort[i].tilStreng())

	def nuværendeKort(self):
		return kort[len(kort)-1]

	def trækKort(self):
		kort.pop()
		return kort[len(kort)-1]

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