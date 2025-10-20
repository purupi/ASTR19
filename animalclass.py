class HummingBird:
	def __init__(self, body_length, wingspan, beak_length, num_species, amt_of_eggs, endangered):
		self.body_length = body_length   #float
		self.wingspan = wingspan   #float
		self.beak_length = beak_length   #float
		self.num_species = num_species
		self.amt_of_eggs = amt_of_eggs   #int
		self.endangered = endangered

	def describe(self):
		print("Description of Hummingbirds:")
		print("Average body Length:", self.body_length)
		print("Average wingspan:", self.wingspan)
		print("Average beak length:", self.beak_length)
		print("Number of species:", self.num_species)
		print("Average amount of eggs:", self.amt_of_eggs)
		print("Are they endangered?", self.endangered)

def main():
	animal = Hummingbird(body_length = 3.9, wingspan = 3.1, beak_length=4.7,num_species=336,amt_of_eggs=2, endangered = False)

	animal.describe()

main()