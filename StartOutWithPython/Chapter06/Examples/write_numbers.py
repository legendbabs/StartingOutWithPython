def main():
	outfile = open('numbers.txt', 'w')

	num1 = int(input('Enter a number: '))
	num2 = int(input('Enter another number: '))
	num3 = int(input('Enter another number: '))

	outfile.write(str(num1) + '\n')
	outfile.write(str(num2) + '\n')
	outfile.write(str(num3) + '\n')

	outfile.close()

	print('Data written to numbers.txt. ')

main()