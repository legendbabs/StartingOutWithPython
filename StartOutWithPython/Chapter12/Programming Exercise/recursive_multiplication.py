def main():
	num1 = int(input('Enter a number: '))
	num2 = int(input('Enter another number: '))

	result = recursive_mul(num1, num2)
	print(num1, '*', num2, 'is:', result)

def recursive_mul(x, y):
	if x > 0 and y > 0:
		return x + recursive_mul(x, y-1)
	else:
		return 0

main()

