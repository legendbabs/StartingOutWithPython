# Create a person class
class Person:
	# Initialize the person attibutes
	def __init__(self, name, address, age, phone):
		self.__name = name
		self.__address = address
		self.__age = age
		self.__phone = phone


	# Create mutator methods for the attributes
	def set_name(self, name):
		self.__name = name

	def set_address(self, address):
		self.__address = address

	def set_age(self, age):
		self.__age = age

	def set_phone(self, phone):
		self.__phone = phone

	# Create thr mutator methods
	def get_name(self):
		return self.__name 

	def get_address(self):
		return self.__address 

	def get_age(self):
		return self.__age 

	def get_phone(self):
		return self.__phone

	# Return the current state of the object
	def __str__(self):
		return 'Name: ' + self.__name + '\n' \
		'Address: ' + self.__address + '\n' \
		'Age: ' + str(self.__age) + '\n' \
		'Phone: ' + self.__phone


# Create the main function
def main():
	# Create 3 objects, one for you, one for
	# your friend and one for your family
	my_personal_info = Person('Tunde Muhamed', 'tundemuhamed@gmail.com', 29, '070-3321-6997')
	my_fiend_info = Person('Shina Onilude', 'shinapee@gmail.com', 30, '081-3262-1388')
	my_family_info = Person('Abodunrin Bashiry', 'ILUPEJU 2, Mosobolatan House.', 63, '080-6076-5926')

	print('These are the details of the personal\ninformation you entered...')
	print('=====================================')
	print()
	print('My Personal Details')
	print('-------------------')
	print(my_personal_info)

	print()
	print('My Friend Details')
	print('-----------------')
	print(my_fiend_info)

	print()
	print('My Personal Member Details')
	print('--------------------------')
	print(my_family_info)

main()



