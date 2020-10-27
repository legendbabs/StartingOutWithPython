# Create an employee class
class Employee:
	def __init__(self, name, id_number, department, job_title):
		self.__name = name
		self.__id = id_number
		self.__dept = department
		self.__title = job_title

	# Create the mutator methods
	def set_name(self, name):
		self.__name = name

	def set_id(self, id_number):
		self.__id = id_number

	def set_department(self, department):
		self.__dept = department

	def set_title(self, job_title):
		self.__title = job_title

	# Create the accessor methods
	def get_name(self):
		return self.__name

	def get_id(self):
		return self.__id

	def get_department(self):
		return self.__dept 

	def get_title(self):
		return self.__title

	def __str__(self):
		return 'Name: ' + self.__name + '\n' \
		'ID Number: ' + self.__id + '\n' \
		'Department: ' + self.__dept + '\n' \
		'Job Title: ' + self.__title


# def main():
# 	# Create three employee objects
# 	emp1 = Employee('Susam Meyers', '47899', 'Accounting', 'Vice President')
# 	emp2 = Employee('Mark Jones', '39119', 'IT', 'Programmer')
# 	emp3 = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')

# 	# Display the data of each employee

# 	print('Here are the datas of the employees...')
# 	print('======================================')
# 	print()

# 	print('EMPLOYEE 1.')
# 	print('-----------')
# 	print('Name:', emp1.get_name())
# 	print('ID Number:', emp1.get_id())
# 	print('Department:', emp1.get_department())
# 	print('Job Title:', emp1.get_title())

# 	print()
# 	print('EMPLOYEE 2.')
# 	print('-----------')
# 	print('Name:', emp2.get_name())
# 	print('ID Number:', emp2.get_id())
# 	print('Department:', emp2.get_department())
# 	print('Job Title:', emp2.get_title())

# 	print()
# 	print('EMPLOYEE 3.')
# 	print('-----------')
# 	print('Name:', emp3.get_name())
# 	print('ID Number:', emp3.get_id())
# 	print('Department:', emp3.get_department())
# 	print('Job Title:', emp3.get_title())

# main()
