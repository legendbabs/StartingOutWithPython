# This program demonstrates the in operator used with a list

def main():
	# Create a list of product numbers
	prod_nums = ['V475', 'F987', 'Q143', 'R688']

	# Get a product number to search for
	search = input('Enter a product number: ')

	# if search in prod_nums:
	if search not in prod_nums:
		print(search, 'was not found in the list.')
	else:
		print(search, 'was found in the list.')

main()
