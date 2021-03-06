# -*- coding: utf-8 -*-

from klasser.spiller import *
from klasser.spil import *

# Brugeren vælger hvor mange spillere, der skal være med. Dette er egentlig bare et spørgsmål om hvor langt spillet skal være, da brugeren kun kan styre én bruger.
# Derefter starter spillet.
# Spillerne (brugeren og x computerstyrede spillere) skiftes til at gætte på om det næste kort er over eller under - brugeren starter.
# Der skrives løbende i kommandolinjen hvad der sker i spillet.
# Dette inkluderer:
# 	* Hvad det nuværende kort er
# 	* Hvad de computerstyrede spillere gør
# 	* Hvad brugeren selv gør
# Hvordan det bliver skrevet og formuleret, kommer dog an på spillerens nuværende promille. Promillen starter på 0. For hver gang brugeren gætter forkert, hæves denne.

def setup():
	print("Velkommen til OverEllerUnder!")
	print("Det bliver sjovt.\n")

	# Spørg om brugerens navn og antal modspillere
	navn = input("Hvad er dit navn? ")
	antalSpillere = int(input("Hvor mange andre spillere vil du spille med? (anbefalet mellem 1 og 5) "))
	
	# 2 blanke linjer
	print()
	print()

	# Opret en bruger med det givne navn.
	bruger = Spiller(navn)

	# Start spillet
	spillet = Spil(bruger, antalSpillere)

setup()