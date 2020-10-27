# Ask user to enter a series of positive numbers
# The user should enter a negative number to signal the end of the series


sum = 0.0

print('Enter a series of +VE numbers or enter -VE numbers to cancel', end='')

number = int(input(': '))

while number > 0:
	sum += number
	print('Enter more positive numbers', end='')

	number = int(input(': '))

print(f'Total: {sum}')






	
