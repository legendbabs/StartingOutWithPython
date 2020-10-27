# The mammal class represents a generic mammal
class Mammal:

	# The __init__ method accept arguments for 
	# The mammal's species
	def __init__(self, species):
		self.__species = species

	# The show species method displays a message
	# indicating the mammal's species
	def show_species(self):
		print('I am a', self.__species)

	# The make sound method is the mammal's
	# way of making a generic sound
	def make_sound(self):
		print('Grrrrr')


# The Dog class is a subclass of mammal class
class Dog(Mammal):
	# The init method calls the superclass's
	# init method passing Dog as the species
	def __init__(self):
		Mammal.__init__(self, 'Dog')

	# the make sound method overrides the superclass's
	# make_sound method
	def make_sound(self):
		print('Woof! woof!')


class Cat(Mammal):
	def __init__(self):
		Mammal.__init__(self, 'Cat')

	def make_sound(self):
		print('Meow')
		