import animals

def main():
	mammal = animals.Mammal('regular animal')
	dog = animals.Dog()
	cat = animals.Cat()

	print('Here are some animals and\nthe sound they make:')
	print('-------------------------')

	show_mammal_info(mammal)
	print()

	show_mammal_info(dog)
	print()

	show_mammal_info(cat)


def show_mammal_info(creature):
	creature.show_species()
	creature.make_sound()

main()
