import spiller

class Spil:
	bruger = None
	aiSpillere = None

	def __init__(self, bruger, antalModstandere):
		self.bruger = bruger

		self.aiSpillere = [antalModstandere]

		for i in range(antalModstandere):
			self.aiSpillere[i] = spiller.AISpiller()

		