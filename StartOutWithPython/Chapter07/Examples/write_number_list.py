# This program writes a list of numbers to a file

def main():
	numbers = [1, 2, 3, 4, 5, 6, 7]
	outfile = open('numberlist.txt', 'w')

	for item in numbers:
		outfile.write(str(item) + '\n')

	outfile.close()

main()