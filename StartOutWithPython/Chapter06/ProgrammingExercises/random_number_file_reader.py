# This program reads the content of the file named random_numbers.txt
# then displays the numbers, displays the total of the numbers, and
# the number of random numbers read from the file.

def main():
	total = 0.0
	count = 0

	infile = open('random_numbers.txt', 'r')

	print('The List Of The Random NUmbers...')
	print('------------------------------')

	for line in infile:
		val = float(line)
		count += 1
		total += val
		print(f'#{count}: {val}')

	print()

	infile.close()

	# display the sum of all the random numbers
	print(f'Total of all random numbers in (random_numbers.txt) file is/are {total}.')

	# Display how many random numbers in the file
	print(f'The number of random numbers in (random_numbers.txt) file is {count}.')

main()