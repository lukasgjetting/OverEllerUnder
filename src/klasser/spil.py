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

		for i in range(0, antalModstandere):
			self.aiSpillere.append(AISpiller())

		self.kortspil = Kortspil()

		self.spilLøkke()
	
	def spilLøkke(self):
		while(self.spilErIGang):
			print("Nuværende kort: " + self.kortspil.nuværendeKort().tilStreng())

			kommandoer = ["o", "u"]

			print("Over eller under, " + self.bruger.navn + "? (indtast \"" + kommandoer[0] + "\" eller \"" + kommandoer[1] + "\")")

			gæt = -1

			while(gæt == -1): 
				brugerInput = input("Dit gæt: ")
				if(brugerInput in kommandoer):
					# Sæt gæt til enten 0 eller 1 hvor over er 0
					gæt = kommandoer.index(brugerInput)
					break
				else:
					print("Forkert input, prøv igen..")

			rigtigt = self.kortspil.trækKort()

			print("Du træk " + self.kortspil.nuværendeKort().tilStreng())

			if(gæt == rigtigt):
				print("Du gættede rigtigt!")
			else: 
				print("Du gættede forkert..")
				print("*" + self.bruger.navn + " tager en tår*")
				self.bruger.hævPromille()
