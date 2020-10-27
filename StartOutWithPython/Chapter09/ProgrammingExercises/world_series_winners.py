def main():
	infile = open('WorldSeriesWinners.txt', 'r')
	line = infile.readlines()
	# Stripthe new line from the list
	for index in range(len(line)):
		line[index] = line[index].rstrip('\n')
#	print(line) Years list from 2009-1903


	# chron_line = line[-1::-1]  # Years list from 1903-2009
	#print(chron_line)

	world_series_count = perf_func(line)
	result_dict = perf_func2(line, world_series_count)

	search_year = int(input('Enter a year between 1903 and 2009: '))
	while search_year == 1904 or search_year == 1994:
		print('There was no world cup in', search_year)
		search_year = int(input('Enter another year: '))

	if search_year in result_dict:
		print(result_dict[search_year], 'won in', search_year)
		print('They won a total of', world_series_count[result_dict[search_year]], 'times')
	else:
		print('That year was not found.')


def perf_func(world_series_list):
	found = False
	world_series_dict = {}
	count_word = 1

	for item in world_series_list:
		if item not in world_series_dict:
			world_series_dict[item] = count_word
		else:
			found =True
			count_word = world_series_dict[item] + 1
			world_series_dict[item] = count_word
		count_word = 1

	#print(world_series_dict)
	return world_series_dict
	print()


def perf_func2(reverse_chron_list, series_dict):
	new_dict = dict()
	skip = False
	year = 1903
	counter = 0

	for item in reverse_chron_list:
		if item.startswith('World'):
			# print(item)
			skip = True
		else:
			new_dict[year] = item
		year += 1
		skip = False

	# for index in range(len(reverse_chron_list)):
	# 	if reverse_chron_list[index].startswith('World'):
	# 		skip = True
	# 	new_dict[year] = reverse_chron_list[index]
	# 	year += 1

	return new_dict


	# print(new_dict)
main()