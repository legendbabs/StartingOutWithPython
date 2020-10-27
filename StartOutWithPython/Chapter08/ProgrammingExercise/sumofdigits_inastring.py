# This program asks the user to enter a string
# and displays the sum, eg 2514 = 12


def main():
	total = 0
	num_str = input('Enter a series of single digit number: ')

	for ch in num_str:
		if ch.isdigit():
			total += int(ch)

	print('Total is:', total)

main()
