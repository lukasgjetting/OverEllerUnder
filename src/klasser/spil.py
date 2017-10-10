from klasser.spiller import *
from klasser.kortspil import *
import time

class Spil:
	bruger = None
	aiSpillere = None
	kortspil = None
	spilErIGang = True

	def __init__(self, bruger, antalModstandere):
		self.bruger = bruger

		self.aiSpillere = []

		for i in range(0, antalModstandere):
			self.aiSpillere.append(AISpiller())

		self.kortspil = Kortspil()

		self.spilLøkke()
	
	def spilLøkke(self):
		while(self.spilErIGang):
			print()
			print()

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

			rigtigt = self.kortspil.trækOgSammenlignKort()

			print("Du trak " + self.kortspil.nuværendeKort().tilStreng())

			if(gæt == rigtigt):
				print("Du gættede rigtigt!")
			else: 
				print("Du gættede forkert..")
				print("*" + self.bruger.navn + " tager en tår*")
				self.bruger.hævPromille()


			for i in range(0, len(self.aiSpillere)):

				print()
				print()

				nuværendeSpiller = self.aiSpillere[i]

				gæt = nuværendeSpiller.gæt(self.kortspil.nuværendeKort())

				# Vent mindst et halvt sekund, og yderligere tid alt efter spillerens promille
				time.sleep(.5 * (nuværendeSpiller.promille + 1))
				print(nuværendeSpiller.navn + " gætter på at næste kort er " + nøgleord[gæt])
				time.sleep(.25)

				if(gæt == self.kortspil.trækOgSammenlignKort()):
					print(nuværendeSpiller.navn + " gættede rigtigt!")
				else:
					print(nuværendeSpiller.navn + " gættede forkert.")
					print("*" + nuværendeSpiller.navn + " tager en tår*")
					nuværendeSpiller.hævPromille()
