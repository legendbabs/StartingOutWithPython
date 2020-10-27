import contact
import pickle

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constants for the file name
FILENAME = 'contacts.dat'

def main():
	# Load the existing contacts dictionary 
	# and ssign it to mycontacts
	mycontacts = load_contacts()

	choice = 0
	while choice != QUIT:
		choice = get_menu_choice()

		if choice == LOOK_UP:
			look_up(mycontacts)
		elif choice == ADD:
			add(mycontacts)
		elif choice == CHANGE:
			change(mycontacts)
		elif choice == DELETE:
			delete(mycontacts)

	# Sve the mycontacts dictionary to a file
	# print(mycontacts)
	save_contacts(mycontacts)


def get_menu_choice():
	print()
	print('Menu')
	print('-----------------------------')
	print('1. Look up a contact')
	print('2. Add a new contact')
	print('3. Change an existing contact')
	print('4. Delete a contact')
	print('5. Quit the program.')

	choice = int(input('Enter your choice: '))
	# Validate the choice
	while choice < LOOK_UP or choice > QUIT:
		choice = int(input('Enter a valid choice: '))
	return choice


def load_contacts():
	try:
		input_file = open(FILENAME, 'rb')
		contact_dct = pickle.load(input_file)

		input_file.close()

	except IOError:
		# Could not open the file, so create
		# an empty dictionary
		contact_dct = {}

	return contact_dct


def look_up(mycontacts):
	name = input('Enter a name: ')
	print(mycontacts.get(name, 'That name is not found.'))


def add(mycontacts):
	name = input('Name: ')
	phone = input('Phone: ')
	email = input('Email: ')

	# Create a contact object named entry
	entry = contact.Contact(name, phone, email)

	if name not in mycontacts:
		mycontacts[name] = entry
		print('The entry has been added.')
	else:
		print('That name already exists.')


def change(mycontacts):
	name = input('Enter a name: ')
	if name in mycontacts:
		# Get a new phone number
		phone = input('Enter a new phone number: ')
		# Get a new email address
		email = input('Enter the new email address: ')

		# Create a contact object named entry
		entry = contact.Contact(name, phone, email)
		mycontacts[name] = entry

		print('Information updated.')

	else:
		print('That name is not found.')


def delete(mycontacts):
	name = input('Enter a name: ')
	if name in mycontacts:
		del mycontacts[name]
		print('Entry deleted.')
	else:
		print('That name is not found.')


def save_contacts(mycontacts):
	output_file = open(FILENAME, 'wb')
	pickle.dump(mycontacts, output_file)
	output_file.close()


main()