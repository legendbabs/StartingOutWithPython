# # This program asks the user to enter the name of a file
# with each line preceded with a line number and a colon

def main():
	count = 0
	filename = input('Enter a file name: ')

	infile = open(filename, 'r')
	for line in infile:
		amount = int(line)
		count += 1
		print('Line Number #', count, ': ', amount, sep='')

	infile.close()

main()