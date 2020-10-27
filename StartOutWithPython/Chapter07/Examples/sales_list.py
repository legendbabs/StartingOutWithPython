# The NUM_DAYS constant holds the number of days that we will gather sales data for

NUM_DAYS = 5

def main():
	# create a list to hold the sales for each day
	sales = [0] * 5

	index = 0

	print('Enter the sales for each day.')

	while index < NUM_DAYS:
		print('Day #', index+1, ': ', sep='', end='')
		sales[index] = float(input())
		index += 1

	# Display the values entered
	print('Here are the values you entered:')
	for value in sales:
		print(value)

main()