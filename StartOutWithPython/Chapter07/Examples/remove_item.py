# This program deonstrates how to use the remove method 
# to remove an item from a list

def main():
	# Create a list with some items
	food = ['Pizza', 'Burgers', 'Chips']

	print('Here are the items in the fod list:')
	print(food)
	print()

	# Get the item to remove
	item = input('Which item do you want to remove? ')

	try:
		food.remove(item)

		print('Here is the revised list:')
		print(food)

	except ValueError:
		print('That item was not found in the list.')

	# except Exception as err:
	# 	print('ERROR !!!:', err)


main()