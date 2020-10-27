def average_price_per_year(dates, prices):
	year = ''
	counter = 0
	accumulator = 0
	average_year_years = []
	average_year_prices = []
	# For every date in the date list, do the following
	for index in range(len(dates)):
		# Set the first year
		if year == '':
			year = dates[index][6:10]
			accumulator += float(prices[index])
			counter += 1

		# Continue with the rest dates if we are 
		# still in the same year then
		elif dates[index][6:10] == year:
			accumulator += float(prices[index])
			counter += 1

		# If the year changed, calculate the average for the
		# year and continue with the next year
		else:
			average = accumulator / counter
			average_year_years.append(year)
			average_year_prices.append(average)
			year = dates[index][6:10]
			counter = 1
			accumulator = float(prices[index])
	# print(average_year_years)
	# print(average_year_prices)
	print('Average Price Per Year')
	print('----------------------')
	print()
	print('Year\t\tPrice')
	print('----\t\t-----')
	for index in range(len(average_year_years)):
		print(average_year_years[index], '\t--->\t', format(average_year_prices[index], '.3f'))


def average_price_per_month(dates, prices):
	month = ''
	year = ''
	counter = 0
	accumulator = 0
	average_price_months = []
	average_price_prices = []

	for index in range(len(dates)):
		if year == '':
			year = dates[index][6:10]
		elif month == '':
			month = dates[index][0:2]
		elif dates[index][0:2] == month and dates[index][6:10] == year:
			accumulator += float(prices[index])
			counter += 1
		else:
			average = accumulator / counter
			average_price_months.append(year + '-' + month)
			average_price_prices.append(average)
			counter = 1
			accumulator = float(prices[index])
			year = dates[index][6:10]
			month = dates[index][0:2]

	print('Average Price Per Month')
	print('-----------------------')
	print()
	print('Month\t\tPrice')
	print('-----\t\t-----')
	for index in range(len(average_price_months)):
	    print(average_price_months[index],'----->\t',format(average_price_prices[index],',.3f'))


def highest_lowest_price_per_year(dates, prices):
	year = ''
	year_list = []
	highest_per_year = []
	lowest_per_year = []
	find_max_min_price = []
	for index in range(len(prices)):
		prices[index] = float(prices[index])

	for index in range(len(dates)):
		if year == '':
			year = dates[index][6:10]
			find_max_min_price.append(prices[index])
		elif dates[index][6:10] == year:
			find_max_min_price.append(prices[index])
		else:
			year_list.append(year)
			highest_per_year.append(max(find_max_min_price))
			lowest_per_year.append(min(find_max_min_price))
			year = dates[index][6:10]
			find_max_min_price = [prices[index]]
	print()

	print('Highest and Lowest Prices Per Year')
	print('----------------------------------')
	print()
	print('Year\tHigh\tLow')
	print('----\t----\t---')
	for index in range(len(year_list)):
	    print(year_list[index],'\t',format(highest_per_year[index],',.3f'),'\t',format(lowest_per_year[index],',.3f'))


def list_of_prices_lowest_highest(dates, prices):
	min_to_max_prices = []
	min_to_max_dates = []
	price_list = []
	date_list = dates[:]

	outfile = open('LowToHigh.txt', 'w')
	for index in range(len(prices)):
		price_list.append(float(prices[index]))
	for count in range(len(price_list)):
		min_to_max_prices.append(min(price_list))
		min_to_max_dates.append(dates[price_list.index(min(price_list))])
		del date_list[price_list.index(min(price_list))]
		del price_list[price_list.index(min(price_list))]

	print('List of Prices, Lowest to Highest')
	print('---------------------------------')
	print()
	print('Date\t\tPrice')
	print('----\t-----')
	for index in range(len(min_to_max_prices)):
		print(min_to_max_dates[index],'\t',min_to_max_prices[index])
		outfile.write(str(min_to_max_dates[index]) + ':' + str(min_to_max_prices[index]) + '\n')
	outfile.close()


def list_of_prices_highest_lowest(dates, prices):
	max_to_min_prices = []
	max_to_min_dates = []
	price_list = []
	date_list = dates[:]

	outfile = open('HighToLow.txt', 'w')
	for index in range(len(prices)):
		price_list.append(float(prices[index]))
	for count in range(len(price_list)):
		max_to_min_prices.append(max(price_list))
		max_to_min_dates.append(dates[price_list.index(max(price_list))])
		del date_list[price_list.index(max(price_list))]
		del price_list[price_list.index(max(price_list))]

	print('List of Prices, Highest to Lowest')
	print('---------------------------------')
	print()
	print('Date\t\tPrice')
	print('----\t-----')
	for index in range(len(max_to_min_prices)):
		print(max_to_min_dates[index],'\t',max_to_min_prices[index])
		outfile.write(str(max_to_min_dates[index]) + ':' + str(max_to_min_prices[index]) + '\n')
	outfile.close()


def main():
	infile = open('GasPrices.txt', 'r')
	infile_list = infile.readlines()
	# print(infile_list)

	date_list = []
	price_lists = []

	for line in infile_list:
		date_list.append(line[0:10])
		price_lists.append(line[11:].rstrip('\n'))

	# print(date_list)
	# print(price_lists)
	infile.close()

	average_price_per_year(date_list, price_lists)
	average_price_per_month(date_list, price_lists)
	highest_lowest_price_per_year(date_list, price_lists)
	list_of_prices_lowest_highest(date_list, price_lists)
	list_of_prices_highest_lowest(date_list, price_lists)
	

main()