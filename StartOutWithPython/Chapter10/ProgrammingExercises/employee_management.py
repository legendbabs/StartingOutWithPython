import employee_class
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Create a file name
FILENAME = 'dictionary.dat'

def main():
	# load the contents of the dictionary
	my_data = load_data()

	# Initialize choice
	choice = 0
	while choice != QUIT:
		choice = display_menu_choice()
		if choice == LOOK_UP:
			look_up(my_data)
		elif choice == ADD:
			add(my_data)
		elif choice == CHANGE:
			change(my_data)
		elif choice == DELETE:
			delete(my_data)

	# save the contents
	save_data(my_data)


def load_data():
	try:
		# Read the contents of a binary file
		input_file = open(FILENAME, 'rb')
		# Load the content of the file
		dictionary_dct = pickle.load(input_file)
		input_file.close()

	except IOError:
		# If there is nothing inside the ditionary
		# then create an empty dictionary
		dictionary_dct = {}

	return dictionary_dct


def display_menu_choice():
	print('MENU')
	print('--------------------------------')
	print('1. Look up an employee ID Number')
	print('2. Add an ID')
	print('3. Change an ID Number')
	print('4. Delete an ID')
	print('5. Quit the program.')

	choice = int(input('Enter Your Choice: '))
	# Validate the choice
	while choice < LOOK_UP or choice > QUIT:
		choice = int(input('Enter a valid choice: '))

	return choice


# Look up function
# Look up an id number in the dictionary
def look_up(my_data):
	id_num = input('Enter an ID Number: ')
	print(my_data.get(id_num, 'ID not found.'))


# add function adds data to the dictionary if not found
def add(my_data):
	id_num = input('Enter an ID Number: ')
	name = input('Enter your name: ')
	dept = input('Enter the department: ')
	title = input('Enter the job title: ')

	# Create an instance of the employee class named entry
	entry = employee_class.Employee(name, id_num, dept, title)

	# If id num not in dictionary, add it as a key with
	# the entry object as value
	if id_num not in my_data:
		my_data[id_num] = entry
		print('The entry has been added.')
	else:
		print('That name already exists.')


def change(my_data):
	id_num = input('Enter an ID: ')
	if id_num in my_data:
		name = input('Enter your name: ')
		dept = input('Enter the department: ')
		title = input('Enter the job title: ')

		entry = employee_class.Employee(name, id_num, dept, title)
		my_data[id_num] = entry
		print('Entry has been updated.')
	else:
		print('That ID was not found.')


def delete(my_data):
	id_num = input('Enter an ID: ')
	if id_num in my_data:
		del my_data[id_num]
		print('Data has been deleted.')
	else:
		print('That ID was not found.')


def save_data(my_data):
	output_file = open(FILENAME, 'wb')
	pickle.dump(my_data, output_file)
	output_file.close()

main()




