class RetailItem:
	def __init__(self, description, units_in_inventory, price):
		self.__descr = description
		self.__inventory = units_in_inventory
		self.__price = price

	def set_description(self, description):
		self.__descr = description

	def set_units_in_inventory(self, units_in_inventory):
		self.__inventory = units_in_inventory

	def set_price(self, price):
		self.__price = price

	def get_description(self):
		return self.__descr 

	def get_units_in_inventory(self):
		return self.__inventory 

	def get_price(self):
		return self.__price

	# Define the str method to return the state of the objects
	def __str__(self):
		return 'Description: ' + self.__descr + '\n' \
		'Units In Inventory: ' + str(self.__inventory) + '\n' \
		'Price: ' + str(self.__price)


def main():
	item1 = RetailItem('Jacket', 12, 59.95)
	item2 = RetailItem('Designer Jeans', 40, 34.95)
	item3 = RetailItem('Shirt', 20, 24.95)

	print('These are the details of each item:')
	print('==================================')
	print()

	print('Item 1.')
	print('------')
	print(item1)
	print()

	print('Item 2.')
	print('------')
	print(item2)
	print()

	print('Item 3.')
	print('------')
	print(item3)

main()

