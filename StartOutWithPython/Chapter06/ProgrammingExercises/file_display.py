# This program writes integer numbers to a file named numbers.txt

def main():
	# create a way to control the loop
	again = 'y'

	# open an output file
	outfile = open('numbers.txt', 'w')

	while again == 'y' or again == 'Y':
		number = int(input('Enter a number: '))
		outfile.write(str(number) + '\n')

		# Enter more numbers
		again = input('Enter [Y/n] to enter another number: ')

	outfile.close()

	print('Integer numbers have been written to numbers.txt.')

# call the main function
main()
