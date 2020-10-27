# This program demonstrates object pickling
import pickle

def main():
	again = 'y'
	# Open a file for binary writing
	output_file  = open('info.dat', 'wb')

	# get data until the user wants to stop
	while again.lower() == 'y':
		# Get data about a person and save it
		save_data(output_file)
		again = input('Enter more data? [Y/n]: ')

	output_file.close()


# The save data function gets data about a person,
# srtores it in a dictionary and then pickles the
# dictionary to the specified file
def save_data(file):
	# Create an empty dictionary
	person = {}

	# Get data for the person and store
	# it in the dictionary
	person['name'] = input('Name: ')
	person['age'] = int(input('Age: '))
	person['weight'] = float(input('Weight: '))

	# Pickle the dictionary
	pickle.dump(person, file)

main()