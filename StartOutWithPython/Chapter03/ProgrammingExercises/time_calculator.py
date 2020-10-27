
BASE_SECONDS = 60
BASE_HOURS = 3600
BASE_DAYS = 86400

print('Enter the number of seconds', end='')
seconds = int(input(': '))

if seconds == BASE_SECONDS:
	minutes_equi = seconds // BASE_SECONDS
	print(f'{seconds} seconds= {minutes_equi}mins')

elif seconds > BASE_SECONDS and seconds < 3600:
	seconds_equi = seconds % BASE_SECONDS
	min_equi = (seconds - seconds_equi) / BASE_SECONDS
	print(f'{seconds} seconds= {min_equi}mins: {seconds_equi}secs')

elif seconds >= 3600 and seconds < 86400:
	hours_remain = seconds % BASE_HOURS
	hours_original = seconds - hours_remain
	hours_equi = hours_original / BASE_HOURS     # Hours Equivalent

	seconds_equi = hours_remain % BASE_SECONDS     # seconds Equivalent

	min_remain = hours_remain - seconds_equi

	min_equi = min_remain / BASE_SECONDS         # Minutes Equivalent
	print(f'{seconds} seconds= {hours_equi}hrs: {min_equi}mins: {seconds_equi}secs')

elif seconds >= 86400:
	days = seconds % BASE_DAYS
	days_remain = seconds - days
	days_equi = days_remain / BASE_DAYS        # Days Equivalent

	hours_remain = seconds % BASE_HOURS
	hours_original = seconds - hours_remain
	hours_equi = hours_original / BASE_HOURS     # Hours Equivalent

	seconds_equi = hours_remain % BASE_SECONDS     # seconds Equivalent

	min_remain = hours_remain - seconds_equi

	min_equi = min_remain / BASE_SECONDS         # Minutes Equivalent
	print(f'{seconds} seconds= {days_equi}days: {hours_equi}hrs: {min_equi}mins: {seconds_equi}secs')
