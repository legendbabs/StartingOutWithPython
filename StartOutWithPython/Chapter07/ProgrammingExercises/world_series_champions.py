def main():
	count = 0
	infile = open('WorldSeriesWinners.txt', 'r')
	winners_list = infile.readlines()

	for index in range(len(winners_list)):
		winners_list[index] = winners_list[index].rstrip('\n')

	search = input('Enter a team\'s name and know how\nmany World Series she has won: ')
	print()

	start_year = 2010
	start_list = []

	# for name in winners_list:
	# 	if name == search:
	# 		count += 1
	# 		start_year -= 1
	# 		start_list.append(start_year)

	for index in range(len(winners_list)):
		start_year -= 1
		if winners_list[index] == search:
			count += 1
			if start_year == 1904 or start_year == 1994:
				break
			start_list.append(start_year)



	print(search.upper(), 'has won World Series Championship', count, 'time(s).')
	print('The years list:', start_list)

main()
