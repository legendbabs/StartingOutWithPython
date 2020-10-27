# This program asks the user to enter the name of a file
# and displays the first 5 lines in the file

def main():
	filename = input('Enter a file name: ')

	infile = open(filename, 'r')
	line1 = infile.readline()
	line2 = infile.readline()
	line3 = infile.readline()
	line4 = infile.readline()
	line5 = infile.readline()

	line1 = line1.rstrip('\n')
	line2 = line2.rstrip('\n')
	line3 = line3.rstrip('\n')
	line4 = line4.rstrip('\n')
	line5 = line5.rstrip('\n')

	infile.close()

	print(line1)
	print(line2)
	print(line3)
	print(line4)
	print(line5)

main()