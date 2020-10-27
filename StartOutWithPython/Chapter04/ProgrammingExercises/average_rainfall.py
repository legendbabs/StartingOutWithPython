MONTHS = 12
years = int(input('Enter the number of years: '))

for yr in range(years):
	print('Year #', yr+1)
	print('========')
	print()

	total = 0.0
	for month in range(MONTHS):
		print('Enter the inches of rainfall for month #',month+1, end='')
		inch = float(input(': '))
		total += inch
	average = total / MONTHS
	print(f'Average Rainfall for year #{yr+1} is: {average:.1f}')
	print()

months_total = years * MONTHS
print(f'Total Number Of Months is: {months_total}')


