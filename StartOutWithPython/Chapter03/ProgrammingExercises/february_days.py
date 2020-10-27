print('Check whether the month February is 28 or 29 days\nif the year is leap...')
print()

year = int(input('Enter the year: '))

if year % 100 == 0 and year % 400 == 0:
	print(f'In {year}, February has 29 days. Therefore {year} is LEAP')
elif year % 100 != 0:
	if year % 4 == 0:
		print(f'In {year}, February has 29 days. Therefore {year} is LEAP')
	else:
		print(f'In {year}, February has 28 days. Therefore {year} is not LEAP')
else:
	print(f'In {year}, February has 28 days. Therefore {year} is not LEAP')
