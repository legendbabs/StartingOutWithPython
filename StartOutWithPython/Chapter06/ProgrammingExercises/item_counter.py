# This program displays the number of names that are stored
# in the file names.txt

def main():
	count = 0
	filename = input('Enter a filename: ')

	infile = open(filename, 'r')

	for line in infile:
		count += 1

	infile.close()

	print(f'Total number of names in this file ({filename}) is {count}.')

main()
