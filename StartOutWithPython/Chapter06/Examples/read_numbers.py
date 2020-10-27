def main():
	infile = open('numbers.txt', 'r')

	num1 = int(infile.readline())
	num2 = int(infile.readline())
	num3 = int(infile.readline())

	infile.close()

	total = num1 + num2 + num3

	print('The numbers are:', num1, num2, num3)
	print('Their total is:', total)


main()