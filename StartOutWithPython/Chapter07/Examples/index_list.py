# This program takes an index of an item in a list
# and assign it to another new item

def main():
	# Create a list of item
	names = ['Tunde', 'Wuraade', 'Tomi']

	print('These are the lists of your names:')
	print(names)

	# Enter an item to search
	name = input('What name do you want to change? ')

	try:
		name_index = names.index(name)

		# Enter a new name
		new_name = input('Enter the new name: ')
		names[name_index] = new_name

		print('Here is the updated lists of names: ')
		print(names)

	except ValueError:
		print('Name was not found in the list.')

main()


