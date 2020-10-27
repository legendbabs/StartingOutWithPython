import employee_production_worker

# main function
def main():
	name = input('Enter the production worker name: ')
	number = input('Enter the production worker number: ')
	shift = int(input('Enter the production worker shift number: '))
	payrate = float(input('Enter the hourly payrate of the worker: '))

	print()
	print('Enter The Shift Supervisor Info')
	name_supo = input('Enter the Shift Supervisor name: ')
	number_supo = input('Enter the Shift Supervisor number: ')
	salary = float(input('Enter the Shift Supervisor Annual Salary: '))
	bonus = float(input('Enter the Shift Supervisor Bonus: '))



	# Create an instance of ProductionWorker class
	production_worker = employee_production_worker.ProductionWorker(name, number, shift, payrate)
	shift_supo = employee_production_worker.ShiftSupervisor(name_supo, number_supo, salary, bonus)
	print()

	# Display the employee datas
	print('These are the ProductionWorker datas:')
	print('=====================================')
	print('Production Worker Name:', production_worker.get_employee_name())
	print('Production Worker Number:', production_worker.get_employee_number())
	# print('Shift Number:', production_worker.get_shift_number(), '===>', end='')

	# Display whether the employee has a day shift or night shift
	if production_worker.get_shift_number() == 1:
		print('YOU WORKED ON DAY SHIFT.')
	elif production_worker.get_shift_number() == 2:
		print('YOU WORKED ON NIGHT SHIFT.')
	else:
		print('Invalid shift number!')

	print('Production Worker Pay Rate: $', format(production_worker.get_hourly_payrate(), ',.2f'), sep='')

	print()
	print('These are the shift supervisor info:')
	print('====================================')
	print()

	print('Shift Supervisor Name:', shift_supo.get_employee_name())
	print('Shift Supervisor Number:', shift_supo.get_employee_number())
	print('Shift Supervisor Salary: $', shift_supo.get_annual_salary(), sep='')
	print('Shift Supervisor Bonus: $', shift_supo.get_annual_production_bonus(), sep='')


main()


