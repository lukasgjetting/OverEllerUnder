from klasser.spiller import *
from klasser.kortspil import *
import konstanter
import time
import sys

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
			
			self.udskriv()
			self.udskriv()

			self.udskriv("Nuværende kort: " + self.kortspil.nuværendeKort().tilStreng())

			kommandoer = [
				self.korrumperKommando(konstanter.nøgleord[0], self.bruger.promille),
				self.korrumperKommando(konstanter.nøgleord[1], self.bruger.promille)
			]

			self.udskriv("Over eller under, " + self.bruger.navn + "? (indtast \"" + kommandoer[0] + "\" eller \"" + kommandoer[1] + "\")")

			gæt = -1

			while(gæt == -1): 
				brugerInput = input("Dit gæt: ")
				if(brugerInput in kommandoer):
					# Sæt gæt til enten 0 eller 1 hvor over er 0
					gæt = kommandoer.index(brugerInput)
					break
				else:
					self.udskriv("Forkert input, prøv igen..")

			rigtigt = self.kortspil.trækOgSammenlignKort()

			self.udskriv("Du trak " + self.kortspil.nuværendeKort().tilStreng())

			if(gæt == rigtigt):
				self.udskriv("Du gættede rigtigt!")
			else: 
				self.udskriv("Du gættede forkert..")
				self.udskriv("*" + self.bruger.navn + " tager en tår*")
				self.bruger.hævPromille()
				
				if(self.bruger.erDød()):
					self.udskriv("Du falder om..")
					time.sleep(1)
					self.udskriv("Du kan ikke holde øjnene åbne..")
					time.sleep(2)
					self.udskriv("Du falder i søvn..")
					time.sleep(3)
					self.udskriv("Du vågner aldrig igen.")
					time.sleep(4)
					self.udskriv("Du er død.")
					time.sleep(2)
					self.udskriv("Du har tabt.")
					time.sleep(10)
					return


			# Liste til at holde styr på de spillere, der dør i denne runde.
			dødeSpillere = []

			# Kør AI-spillerens ture
			for i in range(0, len(self.aiSpillere)):

				self.udskriv()

				nuværendeSpiller = self.aiSpillere[i]

				gæt = nuværendeSpiller.gæt(self.kortspil.nuværendeKort())

				# Vent mindst to sekunder, og yderligere tid alt efter spillerens promille
				time.sleep(2 + (1 * nuværendeSpiller.promille))
				self.udskriv(nuværendeSpiller.navn + " gætter på at næste kort er " + konstanter.nøgleord[gæt])

				rigtigt = self.kortspil.trækOgSammenlignKort()

				self.udskriv(nuværendeSpiller.navn + " trak " + self.kortspil.nuværendeKort().tilStreng())

				if(gæt == rigtigt):
					self.udskriv(nuværendeSpiller.navn + " gættede rigtigt!")
				else:
					self.udskriv(nuværendeSpiller.navn + " gættede forkert.")
					self.udskriv("*" + nuværendeSpiller.navn + " tager en tår*")
					nuværendeSpiller.hævPromille()


				if(nuværendeSpiller.erDød()):
					dødeSpillere.append(nuværendeSpiller)
					self.udskriv(nuværendeSpiller.navn + " er død.")
					self.udskriv("Du er nu ét trin tættere på at vinde.")
					time.sleep(5)

			for i in range(0, len(dødeSpillere)):
				self.aiSpillere.remove(dødeSpillere[i])

	def udskriv(self, besked = ""):
		''' For at undgå at Python bruger en buffer og udskriver alle beskederne på samme tid, skal vi flushe efter hver print-statement. '''
		print(besked)
		sys.stdout.flush()

	def korrumperKommando(self, kommando, promille):
		''' Korrumperer den givne kommando med en intensitetsgrad svarende til den givne promille. '''

		# Lav kommandostrengen om til en liste
		kommandoListe = list(kommando)

		# Indsæt et tilfældigt bogstav på en tilfældig plads i kommandolisten
		for i in range(0, int(promille * 2)):
			kommandoListe.insert(
				random.randint(0, len(kommandoListe)),
				konstanter.bogstaver[random.randint(0, len(konstanter.bogstaver)-1)]
			)

		# Sæt den fuldendte kommando sammen igen og returnér denne.
		return "".join(kommandoListe)