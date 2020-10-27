start_num = float(input('Enter the starting number of organisms: '))
daily_increase = float(input('Enter the daily population increase: '))
days_to_multiply = int(input('Enter the number of days the organisms would be left to multiply: '))

print()
print('Day\tPopulation')
print('==================')

for day in range(1, days_to_multiply+1):
	if day == 1:
		pop = start_num
	else:
		pop = pop + (daily_increase * pop)
	print(f'{day} \t {pop}')

	# elif day == 2:
	# 	pop = pop + (daily_increase * pop)
	# elif day > 2:
	# 	pop = pop + (daily_increase * pop)

def main():
	first_age = int(input('Enter your age: '))
	second_age = int(input('Enter your friend\'s age: ')

	total = sum(first_age, second_age)
	print('Together, you are', total, 'year\'s old')


def sum(num1, num2):
	result = num1 + num2
	return result

main()

