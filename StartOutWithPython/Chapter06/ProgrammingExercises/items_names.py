def main():
	# create a way to control the loop
	again = 'y'

	# open an output file
	outfile = open('names.txt', 'w')

	while again == 'y' or again == 'Y':
		name = input('Enter a name: ')
		outfile.write(name + '\n')

		# Enter more numbers
		again = input('Enter [Y/n] to enter another name: ')

	outfile.close()

	print('Names have been written to names.txt.')

# call the main function
main()