# This program assigns random numbers to a two_dimensional list

import random

ROWS = 3
COLS = 4

def main():
	values = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0]
	]

	# Fill in the lists with random numbers
	for r in range(ROWS):
		for c in range(COLS):
			values[r][c] = random.randint(1, 100)

	# Display the random numbers
	print(values)

	print()
	for r in range(ROWS):
		for c in range(COLS):
			print(values[r][c])

main()