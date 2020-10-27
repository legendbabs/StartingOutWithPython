import login

def main():
	again = 'y'
	while again == 'y' or again == 'Y':
		first_name = input('Enter your first name: ')
		last_name = input('Enter your last name: ') 
		id_number = input('Enter your student ID number: ')

		# print('Your system login name is:')
		password = login.get_login_name(first_name, last_name, id_number)

		while not 

		if login.validate_password(password):
			print('Welcome. Login Successful!!!')
		else:
			print('Invalid password.')
		again = input('Start the process again: ')

		# print()

		# print('Enter your password: ')
		# password = input()
		# while not login.validate_password(password):
			# print('Enter a valid password!')
			# password = input(': ')

		# print('Welcome, your login is successful.')


main()