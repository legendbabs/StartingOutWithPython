# Create an employee class

class Employee:
	# initialize the attributes
	def __init__(self, employee_name, employee_number):
		self.__employee_name = employee_name
		self.__employee_number = employee_number

	# Create the mutator methods
	def set_employee_name(self, employee_name):
		self.__employee_name = employee_name

	def set_employee_number(self, employee_number):
		self.__employee_number = employee_number

	# create the accessor methods
	def get_employee_name(self):
		return self.__employee_name 
	def get_employee_number(self):
		return self.__employee_number 


# Create a production worker class 
class ProductionWorker(Employee):
	def __init__(self, employee_name, employee_number, shift_number, hourly_pay):

		# Call the superclass init method
		Employee.__init__(self, employee_name, employee_number)

		# Initialize the producton class attributes
		self.__shift_number = shift_number
		self.__hourly_payrate = hourly_pay

	# Mutator methods
	def set_shift_number(self, shift_number):
		self.__shift_number = shift_number

	def set_hourly_payrate(self, hourly_pay):
		self.__hourly_payrate = hourly_pay

	# Gettor methods
	def get_shift_number(self):
		return self.__shift_number 

	def get_hourly_payrate(self):
		return self.__hourly_payrate 


# Create a ShiftSupervisor class
class ShiftSupervisor(Employee):
	def __init__(self, employee_name, employee_number, annual_salary, annual_production_bonus):
		# Call the Employee class __init__ method
		Employee.__init__(self, employee_name, employee_number)

		# Initialize the salary and bonus attributes
		self.__annual_salary = annual_salary
		self.__annual_production_bonus = annual_production_bonus

	# Create the settor method for salary and bonus
	def set_annual_salary(self, annual_salary):
		self.__annual_salary = annual_salary

	def set_annual_production_bonus(self, annual_production_bonus):
		self.__annual_production_bonus = annual_production_bonus

	# Create the gettor methods
	def get_annual_salary(self):
		return self.__annual_salary 

	def get_annual_production_bonus(self):
		return self.__annual_production_bonus 
