# This program determines whether a bank customer qualifies for a loan

MIN_SALARY = 30000
MIN_YEAR = 2

salary = float(input('Enter your annual salary: '))
years_on_job = int(input('Enter the number of years employed: '))

# if salary >= MIN_SALARY and years_on_job >= MIN_YEAR:
# 	print('You qualify for the loan.')
# else:
# 	print('You do not qualify for the loan.')

if salary >= MIN_SALARY:
	if years_on_job >= MIN_YEAR:
		print('You qualify for the loan.')
	else:
		print(f'You must have been on the job for at least {MIN_YEAR} years to qualify for the loan..')

else:
	print(f'You must earn at least ${MIN_SALARY} to qualify for the loan.')