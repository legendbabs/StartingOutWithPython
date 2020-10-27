# This program writes a series of random numbers to a file
# Each random number should be in the range of 1 through 500
# The program should specify how many random numbers the file should hold

import random

def main():
	num_rand = int(input('How many random numbers do you want this file to hold? '))

	outfile = open('random_numbers.txt', 'w')

	for num in range(1, num_rand+1):
		rand_num = random.randint(1, 500)
		outfile.write(str(rand_num) + '\n')

	outfile.close()

	print('Random Numbers have been written to random_numbers.txt.')

main()