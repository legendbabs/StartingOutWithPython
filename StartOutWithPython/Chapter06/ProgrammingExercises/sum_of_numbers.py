# This program calculates the total of the numbers in
# the file named numbers.txt

def main():
	total = 0.0

	infile = open('numbers.txt', 'r')

	for line in infile:
		val = float(line)
		total += val

	infile.close()

	print(f'The total of all numbers in the file (numbers.txt) is/are {total:.1f}.')

main()