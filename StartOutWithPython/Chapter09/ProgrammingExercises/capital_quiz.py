# This program creates a dictionary containing US states as 
# keys and their capitals as value. The program randomly quiz the 
# userby displaying the name of a state and asking the user to enter
# that state capital.

def main():
	# Create a dictionary
	state_and_their_capitals = {
	'Abia':'Umaya', 'Adamawa':'Yola', 'Akwa Ibom': 'Uyo', 
	'Bauchi':'Bauchi', 'Delta':'Asaba', 'Lagos':'Ikeja',
	'Niger':'Minna', 'Ogun':'Abeokuta', 'Ondo':'Akure',
	'Oyo':'Ibadan', 'Osun':'Osogbo', 'River':'Portercort',
	'Sokoto':'Sokoto', 'Kano':'Kano', 'Kaduna':'Kaduna',
	'Kwara':'Ilorin', 'Edo':'Benin city','Ekiti':'Ado Ekiti',
	'Kogi':'Lokoja','Imo':'Oweri','FCT':'Abuja'
	}

	count_right = 0  # count correct answers
	count_wrong = 0  # count wrong answers

	# create a means to control the loop
	again = 'y'
	while again.lower() == 'y':
		state, capital = state_and_their_capitals.popitem()
		print('What is the capital of', state, end='')
		ans = input(': ')
		if ans.lower() == capital.lower():
			print('Your answer is correct.')
			count_right += 1
		else:
			print('Wrong!!! The capital of', state, 'is', capital, '.')
			count_wrong += 1

		print()

		again = input('Do you wish to do more test? [Y/n]: ')


	print('You answered', count_right, 'questions correctly\nand you missed.',count_wrong, 'questions')

main()