# This is a math quiz program

import random

MIN = 1
MAX = 1000

def main():
	# Ask the user to enter two numbers and find their sum
	print()
	print('Welcome To Random Math Quiz')
	print('===========================')
	print('If you are sure of yourself, let get started then...')
	print()
	input('Press (Enter) to continue...')

	again = 'y'
	while again == 'y' or again == 'Y':
		num1 = random.randint(MIN, MAX)
		num2 = random.randint(MIN, MAX)

		print('Solve the following:', num1, '+' , num2, '=?')

		result = num1 + num2

		ans = int(input('Enter your answer: '))
		if ans == result:
			print('Congratulations!!! Your answer is correct.')
		else:
			print('Sorry, the correct answer is',result)
		print()

		again = input('Do you wanna perform more quiz? Enter [Y/n] to continue: ')

	print()

	print('Ooch!!! You are leaving? ')
	print('We hope you\'ll be back again in the future to take more quizzes.')


main()


