# This program gets a person first, middle and last names
# and displays their first, middle and last initials

def main():
	first = input('Enter your first name: ')
	middle = input('Enter your middle name: ')
	last = input('Enter your last name: ')

	my_initials = get_initials(first, middle, last)
	print('Your initials is: ', end='')
	print(my_initials)


def get_initials(first_name, middle_name, last_name):
	set1 = first_name[0]
	set2 = middle_name[0]
	set3 = last_name[0]

	initials = set1 + '.' + set2 + '.' + set3
	return initials

main()