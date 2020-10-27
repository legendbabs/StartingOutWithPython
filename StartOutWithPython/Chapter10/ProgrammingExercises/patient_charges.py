# This is the patient's class
class Patient:
	# Create patients attributes
	def __init__(self, first_name, mid_name, last_name, address, city, state, zip_code, number, emer_name, emer_phone):
		self.__first_name = first_name
		self.__mid_name = mid_name
		self.__last_name = last_name
		self.__address = address
		self.__city = city
		self.__state = state
		self.__zip_code = zip_code
		self.__number = number
		self.__emergency_name = emer_name
		self.__emergency_phone = emer_phone

	# create the settor and gettor for the Patients class
	# Settor methods
	def set_first_name(self, first_name):
		self.__first_name = first_name

	def set_middle_name(self, mid_name):
		self.__mid_name = mid_name

	def set_last_name(self, last_name):
		self.__last_name = last_name

	def set_address(self, address):
		self.__address = address

	def set_city(self, city):
		self.__city = city

	def set_state(self, state):
		self.__state = state

	def set_zip_code(self, zip_code):
		self.__zip_code = zip_code

	def set_number(self, number):
		self.__number = number

	def set_emergency_name(self, emer_name):
		self.__emergency_name = emer_name

	def set_emergency_phone(self, emer_phone):
		self.__emergency_phone = emer_phone

	# Gettor methods
	def get_first_name(self):
		return self.__first_name 

	def get_middle_name(self):
		return self.__mid_name 

	def get_last_name(self):
		return self.__last_name 

	def get_address(self):
		return self.__address 

	def get_city(self):
		return self.__city 

	def get_state(self):
		return self.__state 

	def get_zip_code(self):
		return self.__zip_code 

	def get_number(self):
		return self.__number 

	def get_emergency_name(self):
		return self.__emergency_name

	def get_emergency_phone(self):
		return self.__emergency_phone

	# Create a __str__ method that returns the curent state of the objects
	def __str__(self):
		return 'First Name: ' + self.__first_name + '\n' \
		'Middle Name: ' + self.__mid_name + '\n' \
		'Last Name: ' + self.__last_name + '\n' \
		'Address: ' + self.__address + '\n' \
		'City: ' + self.__city + '\n' \
		'State: ' + self.__state + '\n' \
		'Zip Code: ' + self.__zip_code + '\n' \
		'Phone Number: ' + self.__number + '\n' \
		'Emergency Name: ' + self.__emergency_name + '\n' \
		'Emergency Phone Number: ' + self.__emergency_phone



# Create  class named Procedure that represents 
# the medical procedure that has been performed on a patient
class Procedure:
	def __init__(self, procedure_name, procedure_date, practitioner_name, procedure_charges):
		self.__procedure_name = procedure_name
		self.__procedure_date = procedure_date
		self.__practitioner_name = practitioner_name
		self.__procedure_charges = procedure_charges

	# Create settor for the attributes
	def set_procedure_name(self, procedure_name):
		self.__procedure_name = procedure_name

	def set_procedure_date(self, procedure_date):
		self.__procedure_date = procedure_date

	def set_practitioner_name(self, practitioner_name):
		self.__practitioner_name = practitioner_name

	def set_procedure_charges(self, procedure_charges):
		self.__procedure_charges = procedure_charges

	# Create gettor methods

	def get_procedure_name(self):
		return self.__procedure_name 

	def get_procedure_date(self):
		return self.__procedure_date 

	def get_practitioner_name(self):
		return self.__practitioner_name 

	def get_procedure_charges(self):
		return self.__procedure_charges 

	# Create a __str__ method that returns the curent state of the objects
	def __str__(self):
		return 'Name Of Procedure: ' + self.__procedure_name + '\n' \
		'Date Of Procedure: ' + self.__procedure_date + '\n' \
		'Name Of The Practioner: ' + self.__practitioner_name + '\n' \
		'Charges For The Procedure: ' + str(self.__procedure_charges)


# define the main function
def main():
	# Create an instance of the patients class
	patient = Patient('Tunde', 'Muhamed', 'Salami', 'tundemuhamed@gmail.com', 'IBADAN', \
		'Oyo State', '10001', '070-3321-6997', 'Abodunrin Bashiru', '080-6076-5926')

	# Create three instances of the procedure class
	procedure1 = Procedure('Physical Exam', '22/09/2020', 'Dr. Irvine', 250.00)
	procedure2 = Procedure('X-ray', '22/09/2020', 'Dr. Jamison', 500.00)
	procedure3 = Procedure('Blood Test', '22/09/2020', 'Dr. Smith', 200.00)

	# Print the patients details
	print('These are the patient\'s details:')
	print('=================================')
	print()
	print(patient)

	print()
	print('These are the procedures:')
	print('========================')
	print()

	print('PROCEDURE 1.')
	print('------------')
	print(procedure1)
	print()

	print('PROCEDURE 2.')
	print('------------')
	print(procedure2)
	print()

	print('PROCEDURE 3.')
	print('------------')
	print(procedure3)

main()




