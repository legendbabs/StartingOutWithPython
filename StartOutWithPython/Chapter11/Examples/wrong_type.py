import animals

def main():
	# mammal = animals.Mammal('regular animal')
	# dog = animals.Dog()
	# cat = animals.Cat()

	# print('Here are some animals and\nthe sound they make:')
	# print('-------------------------')

	# show_mammal_info(mammal)
	# print()

	# show_mammal_info(dog)
	# print()

	# show_mammal_info(cat)
	# print()

	# Pass a wrong object to the show_mammal function
	show_mammal_info('I am a string')


def show_mammal_info(creature):
	creature.show_species()
	creature.make_sound()

main()