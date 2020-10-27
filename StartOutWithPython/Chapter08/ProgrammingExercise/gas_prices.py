def main():
	# open GasPrices.txt in read mode
	infile = open('GasPrices.txt', 'r')

	# Read the contents of the file into a list
	gas_list = infile.readlines()
	# print(gas_list)

	# strip \n from the list
	price = []
	date = []
	month = []
	day = []
	year = []

	for i in range(len(gas_list)):
		gas_list[i] = gas_list[i].rstrip('\n')
		gas_list[i] = gas_list[i].split(':')
		price.append(gas_list[i][1])
		date.append(gas_list[i][0])
		date[i] = date[i].split('-')
		month.append(date[i][0])
		day.append(date[i][1])
		year.append(date[i][2])

	infile.close()

	average_price(year, price, date)
	sorted_price(gas_list, price)

	# print(gas_list)


def average_price(year, price, date):
	yearly_total = 0
	year_list = list(set(year))
	year_list.sort()
	yt_list = []

	for item in year_list:
		for i in range(len(year)):
			if year[i] == item:
				yearly_total += float(price[i])
		yt_list.append(yearly_total)
		yearly_total = 0

	total = 0
	for item in yt_list:
		total += item
	avg = format(total / len(yt_list), '.3f')
	avg_month = format((float(avg) / 12), '.3f')

	min_price = price.index(min(price))
	max_price = price.index(max(price))

	min_date = date[min_price]
	max_date = date[max_price]

	# print(min_date)
	# print(max_date)

	print('The average price of gas per year is $ ', avg, sep='')
	print('The average price of gas per month is $ ', avg_month, sep='')
	print(f'Minimum gas price is ${min(price)}, on {min_date[0]}-{min_date[1]}-{min_date[2]}')
	print(f'Maximum gas price is ${max(price)}, on {max_date[0]}-{max_date[1]}-{max_date[2]}')

	print()


def sorted_price(date, price):
	# print(date)
	date1 = date
	for i in range(len(date1)):
		# date1.sort()
		# print(date1)
		date1[i][0], date1[i][1] = date1[i][1], date1[i][0]
	date1.sort()
	print(date1)
	date2 = date1[-1::-1] # From highest to lowest 
	# print(date2)
	outfile1 = open('gas_lowest.txt', 'w')
	outfile2 = open('gas_highest.txt', 'w')

	# Write datas to file
	for item in date1:
		dt = item[1]
		pr = item[0]
		outfile1.write(str(dt) + ' ' + str(pr) + '\n')

	for item in date2:
		dt = item[1]
		pr = item[0]
		outfile2.write(str(dt) + ' ' + str(pr) + '\n')

	outfile1.close()
	outfile2.close()

	print('Datas has been successfully written to gas_lowest.txt')
	print('and gas_highest.txt.')


main()