# This program calculates the average of the numbers in
# the file named numbers.txt

def main():
	total = 0.0
	count = 0

	infile = open('numbers.txt', 'r')

	for line in infile:
		val = float(line)
		count += 1
		total += val

	infile.close()

	average = total / count

	print(f'The average of all numbers in the file (numbers.txt) is {average:.1f}.')

main()