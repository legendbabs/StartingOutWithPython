def main():
	date_str = input('Enter a date in the form (mm/dd/yyyy) : ')
	date_split = date_str.split('/')

	date_val = get_date(date_split)
	print(f'The date is: {date_val} {date_split[1]}, {date_split[2]}')

	# print(date_split)

def get_date(date_split):

	if date_split[0] == '01':
		val = 'January'
	elif date_split[0] == '02':
		val = 'February'
	elif date_split[0] == '03':
		val = 'March'
	elif date_split[0] == '04':
		val = 'April'
	elif date_split[0] == '05':
		val = 'May'
	elif date_split[0] == '06':
		val = 'June'
	elif date_split[0] == '07':
		val = 'July'
	elif date_split[0] == '08':
		val = 'August'
	elif date_split[0] == '09':
		val = 'Seotempber'
	elif date_split[0] == '10':
		val = 'Octomber'
	elif date_split[0] == '11':
		val = 'November'
	elif date_split[0] == '12':
		val = 'December'
	return val


main()