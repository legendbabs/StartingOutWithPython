import employee_production_worker

def main():
	shift_supo = employee_production_worker.ShiftSupervisor('Tunde Muhamed', '070-3321-6997', 15000.0, 3500.0)
	print('These are the shift supervisor info:')
	print('====================================')
	print()

	print('Supervisor Name:', shift_supo.get_employee_name())
	print('Supervisor Number:', shift_supo.get_employee_number())
	print('Salary: $', shift_supo.get_annual_salary(), sep='')
	print('Bonus: $', shift_supo.get_annual_production_bonus(), sep='')

main()