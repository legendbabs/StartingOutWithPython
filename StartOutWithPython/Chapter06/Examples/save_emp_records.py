# This program gets employee data from the user and 
# saves it as record in the employees.txt files

def main():
	# Get the number of employees records to create
	num_emps = int(input('How many employee records do you want to create? '))

	# open a file for writing
	emp_file = open('employees.txt', 'w')
	# Get the employee's data and write it to the file
	for count in range(1, num_emps+1):
		print('Enter data for employee #', count, sep='')
		name = input('Name: ')
		id_number = input('ID number: ')
		dept = input('Department: ')

		# write the data as a record to the file

		emp_file.write(name + '\n')
		emp_file.write(id_number + '\n')
		emp_file.write(dept + '\n')
		print()

	emp_file.close()
	print('Employee records written to employee.txt.')

main()