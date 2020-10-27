# Create a person class

class Person:
	def __init__(self, name, address, number):
		self.__name = name
		self.__address = address
		self.__number = number

	# Settor methods
	def set_name(self, name):
		self.__name = name

	def set_address(self, address):
		self.__address = address

	def set_number(self, number):
		self.__number = number

	# Gettor methods
	def get_name(self):
		return self.__name

	def get_address(self):
		return self.__address 

	def get_number(self):
		return self.__number 


class Customer(Person):
	def __init__(self, name, address, number, wishes_to_be_on_a_mailing_list = False):
		Person.__init__(self, name, address, number)

		self.__wishes_to_be_on_a_mailing_list = wishes_to_be_on_a_mailing_list

	def set_wishes(self, wishes_to_be_on_a_mailing_list):
		self.__wishes_to_be_on_a_mailing_list = wishes_to_be_on_a_mailing_list

	def get_wishes(self):
		return self.__wishes_to_be_on_a_mailing_list 


def main():

	customer = Customer('Tunde Muhamed', 'tm@gmail.com', '070-3321-6997')
	print('Customer Name:', customer.get_name())
	print('Customer Address:', customer.get_address())
	print('Customer Number:', customer.get_number())

	# print('Do you wish to be on the mailing list? (Y/n):', end='')
	# response = input()

	# if response.lower() == 'y':
	if customer.get_wishes():
		print('You wish to be on the mailing list.')
	else:
		print('You wish not to be on the mailing list.')


main()

		


