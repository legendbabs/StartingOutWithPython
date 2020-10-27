# This program ask a user to enter a number 
# and find its factorial

print('Finding Factorials Of Numbers...')
num = 1

number = int(input('Enter a number: '))
for n in range(1, number+1):
	num = num * n 

print(f'The factorial of {number} is: {num}')
