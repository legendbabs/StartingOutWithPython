# Ask the user to enter the number of days

num_days = int(input('Enter the number of days: '))
print()
total = 0.0

print('Days\tSalary(Pennies)')
print('=======================')

for day in range(1, num_days+1):
	if day == 1:
		salary = day

    # Salaries for days 2 and above
	else:
		salary = salary * 2
		total += salary

	print(f'{day} \t {salary}')

print()

# Convert pennies to dollars by multiplying by 350

total_salary_in_dollars = total / 350
print(f'Total Salary for {num_days} days is: ${total_salary_in_dollars:,.1f}')


