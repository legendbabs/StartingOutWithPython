# This program reads the contents of the golf.txt file
# and displays the on the screen

def main():

	again = 'y'

	golf_file = open('golf.txt', 'r')

	# read the first line
	name = golf_file.readline()
	while name != '':
		score = float(golf_file.readline())

		# strip the newline
		name = name.rstrip('\n')

		# Display the contents of the file
		print('Name:', name)
		print('Score:', score)
		print()

		name = golf_file.readline()

	golf_file.close()

main()


