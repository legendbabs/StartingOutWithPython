# This program displays the day of the week corresponding 
# to the numbers 1 through 7

MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7

for trial in range(3):
	user_input = int(input('Enter a value, (1 through 7): '))
	if user_input == MONDAY:
		print(f'{user_input} corresponds to Monday')
	elif user_input == TUESDAY:
		print(f'{user_input} corresponds to Tuesday')
	elif user_input == WEDNESDAY:
		print(f'{user_input} corresponds to Wednesday')
	elif user_input == THURSDAY:
		print(f'{user_input} corresponds toThursday')
	elif user_input == FRIDAY:
		print(f'{user_input} corresponds to Friday')
	elif user_input == SATURDAY:
		print(f'{user_input} corresponds to Saturday')
	elif user_input == SUNDAY:
		print(f'{user_input} corresponds to Sunday')
	else:
		print(f'Error!!! {user_input} out of range.')