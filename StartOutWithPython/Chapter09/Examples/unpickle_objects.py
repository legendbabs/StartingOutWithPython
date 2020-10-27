# This program demonstrates object unpickling
import pickle

def main():
	end_of_file = False
	# Open a file for binary reading
	input_file = open('info.dat', 'rb')
	while not end_of_file:
		try:
			person = pickle.load(input_file)
			display_data(person)
		except EOFError:
			# Set the flag to indicate the end of the file
			# has been reached
			end_of_file = True

	input_file.close()


def display_data(person):
	print('Name:', person['name'])
	print('Age:', person['age'])
	print('Weight:', person['weight'])
	print()

main()
