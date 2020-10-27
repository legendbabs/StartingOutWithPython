def main():
	import random

	menu()
	user_guess = int(input('Enter your choice: '))
	print()
	counter = 1
	user_accumulator = 0
	comp_accumulator = 0
	tie_accumulator = 0

	while user_guess != 4:
		number = random.randint(1, 3)

		choice1 = comp_choice_value(number)
		print('ROUND', counter)
		print('The computer choice is', choice1)

		choice2 = user_choice_value(user_guess)
		print('Your choice is', choice2)

		print()
		print('ROUND', counter, 'RESULT')

		result = choice(choice1, choice2)

		if result == 'user':
			print('Congratulations, You won this round.')

			user_accumulator += 1

			if choice2 == 'Rock' and choice1 == 'Scissors':
				print('Rock smashes Scissors.')
			elif choice2 == 'Scissors' and choice1 == 'Paper':
				print('Scissors cuts Paper.')
			elif choice2 == 'Paper' and choice1 == 'Rock':
				print('Paper wraps Rock.')
			print()

			menu()
			user_guess = int(input('Enter your choice: '))
			if user_guess != 4:
				counter += 1
			print()

		elif result == 'none':
			print('This round is tie.')
			tie_accumulator += 1

			print()

			menu()
			user_guess = int(input('Enter your choice: '))
			if user_guess != 4:
				counter += 1
			print()

		else:
			print('You lost, Computer won this round.')
			comp_accumulator += 1

			if choice1 == 'Rock' and choice2 == 'Scissors':
				print('Rock smashes Scissors.')
			elif choice1 == 'Scissors' and choice2 == 'Paper':
				print('Scissors cuts Paper.')
			elif choice1 == 'Paper' and choice2 == 'Rock':
				print('Paper wraps Rock.')

			print()

			menu()
			user_guess = int(input('Enter your choice: '))
			if user_guess != 4:
				counter += 1
			print()

	print()
	print('TOTAL ROUND PLAYED:', counter, 'ROUNDS')
	print('=====================================')
	print('Computer wins', comp_accumulator, 'round(s).')
	print('You win', user_accumulator, 'Round(s).')
	print('There are', tie_accumulator, 'draw(s)')

	print()

	win = win_rate(user_accumulator, comp_accumulator)

	if comp_accumulator > user_accumulator:
		print(f'Buddy, you lost this game. Computer has {win}% win rate, but you have {100-win}% win rate.')
		print('Thanks.')
	elif user_accumulator > comp_accumulator:
		print(f'Congratulations, you won this game with {win}% win rate.')
	else:
		print(f'Your game with the computer is drawn, {50}% win rate each.')
		print('Thanks.')


def win_rate(user_accumulator, comp_accumulator):
	total = user_accumulator + comp_accumulator
	if user_accumulator > comp_accumulator:
		percentage = (user_accumulator / total) * 100
		return percentage
	else:
		percentage = (comp_accumulator / total) * 100
		return percentage


def menu():
	print('===========================')
	print('Rock, Paper & Scissors Game')
	print('===========================')
	print('\tManu')
	print('1) Choice For Rock')
	print('2) Choice For Paper')
	print('3) Choice For Scissors')
	print('4) Quit')


def comp_choice_value(num):
	if num == 1:
		value = 'Rock'
		return value
	elif num == 2:
		value = 'Paper'
		return value
	elif num == 3:
		value = 'Scissors'
		return value


def user_choice_value(user_guess):
	if user_guess == 1:
		value = 'Rock'
		return value
	elif user_guess == 2:
		value = 'Paper'
		return value
	elif user_guess == 3:
		value = 'Scissors'
		return value
	elif user_guess == 4:
		value = 'Quit'
		return value


def choice(number, user_guess):
	if number == 'Rock' and user_guess == 'Paper':
		win = 'user'
		return win
	elif number == 'Paper' and user_guess == 'Rock':
		win = 'computer'
		return win
	elif number == 'Paper' and user_guess == 'Scissors':
		win = 'user'
		return win
	elif number == 'Scissors' and user_guess == 'Paper':
		win = 'computer'
		return win
	elif number == 'Rock' and user_guess == 'Scissors':
		win = 'computer'
		return win
	elif number == 'Scissors' and user_guess == 'Rock':
		win = 'user'
		return win
	else:
		win = 'none'
		return win


main()
