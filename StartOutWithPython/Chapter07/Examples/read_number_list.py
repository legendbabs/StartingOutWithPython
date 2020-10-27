def main():
	infile = open('numberlist.txt', 'r')
	numbers = infile.readlines()

	index = 0
	while index < len(numbers):
		numbers[index] = int(numbers[index])
		index += 1

	infile.close()

	print(numbers)

main()