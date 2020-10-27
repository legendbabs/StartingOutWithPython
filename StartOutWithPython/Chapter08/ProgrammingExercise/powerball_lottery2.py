# # Powerball Lottery

# # Create a pbnumbers.txt file
# # 5 numbers in the range of 1-69
# # 1 number in the range of 1-26

# import random

# def lottery():
# 	numbers = []
# 	powerballs = []

# 	for i in range(5):
# 		number = str(random.randint(1, 69))
# 		if len(number) == 1:
# 			number = '0' + number
# 		numbers.append(number)

# 	# print(numbers)

# 	powerball = str(random.randint(1, 26))
# 	if len(powerball) == 1:
# 		powerball = '0' + powerball
# 	powerballs.append(powerball)

# 	# print(powerballs)

# 	winning_numbers_list = numbers + powerballs
# 	# print(winning_numbers_list)

# 	winning_numbers = ''
# 	for number in winning_numbers_list:
# 		winning_numbers += number + ' '
# 	# print(winning_numbers)

# 	winning_numbers = winning_numbers.rstrip()
# 	return winning_numbers

# 	# print(winning_numbers)

# # lottery()
# def main():
# 	outfile = open('pbnumbers.txt', 'w')
# 	for i in range(1, 655):
# 		line = lottery()
# 		# print(line)
# 		outfile.write(line + '\n')

# 	outfile.close()

# main()


def unified_list(number_list):
	master_list = []
	for draw in number_list:
		draw_list = draw.split()
		# print(draw_list)
		master_list += draw_list
	# print(master_list)
	# print(draw_list)
	return master_list, draw_list


def times_each_appear(a_list):
	counter = 0
	numbersfound = []
	timesfound = []

	# Iterate each number in the list
	for number in a_list:
		if number not in numbersfound:
			# Set up a counter to check how many times the number is seen
			counter = 0

			# Check how many times the number is in this list
			for searchnumber in a_list:
				# If the number is found, add 1 to the counter
				if number == searchnumber:
					counter += 1

		if number not in numbersfound:
			numbersfound.append(number)
			timesfound.append(counter)

	return numbersfound, timesfound

	# print(numbersfound)
	# print()
	# print()
	# print(timesfound)


def top_ten_common(times, numbers):
	counter = 0
	index = 0
	top_10_times = []
	top_10_numbers = []

	for count in range(10):
		# Find the index number of the number that appear most times
		index = times.index(max(times)) 
		# Add this number to the list top10numbers
		top_10_numbers.append(numbers[index])
		# Add the number of times it was found to top10times
		top_10_times.append(times[index])
		# Delete the numbers from the search list
		del numbers[index]
		del times[index]

	print('Most Common Numbers')
	print('-------------------')
	print()
	print('Number\t\tTimes')
	print('------\t\t-----')
	print()

	for index in range(len(top_10_numbers)):
		print(top_10_numbers[index] + '\t--->\t' + str(top_10_times[index]))
	print()


def bottom_ten_common(times, numbers):
	counter = 0
	index = 0
	bottom_10_times = []
	bottom_10_numbers = []

	for count in range(10):
		# Find the index number of the number that appear the least times
		index = times.index(min(times)) 
		# Add this number to the list bottom10numbers
		bottom_10_numbers.append(numbers[index])
		# Add the number of times it was found to bottom10times
		bottom_10_times.append(times[index])
		# Delete the numbers from the search list
		del numbers[index]
		del times[index]

	print('Least Common Numbers')
	print('-------------------')
	print()
	print('Number\t\tTimes')
	print('------\t\t-----')
	print()

	for index in range(len(bottom_10_numbers)):
		print(bottom_10_numbers[index] + '\t--->\t' + str(bottom_10_times[index]))
	print()


def top_10_overdue(times, numbers, original_list):
	count = 0
	overdue_list = []
	not_seen_list = []
	placeholder = ''

	for number in numbers:
		placeholder = number

		for specific_number in numbers:
			if specific_number == placeholder:
				count = 0
			else:
				count += 1

		overdue_list.append(number)
		not_seen_list.append(count)
	# print(numbers)
	# print(overdue_list)
	# print(not_seen_list)

	top_10_overdue = []
	top_10_not_seen_for= []
	for count in range(10):
		index = not_seen_list.index(max(not_seen_list))
		top_10_not_seen_for.append(not_seen_list[index])
		top_10_overdue.append(overdue_list[index])
		del not_seen_list[index]
		del overdue_list[index]
	print("Overdue List")
	print("------------")
	print()
	print('Number\t\tOverdue')
	print('------\t\t-------')
	for index in range(len(top_10_overdue)):
	    print(top_10_overdue[index] + '\t--->\t' + str(top_10_not_seen_for[index]))
	print()


def separate_frequency(a_list):
	powerballs = []
	powerballs_count = []
	non_powerballs = []
	non_powerballs_count = []
	counter = 0
	number = 0

	for count in range(1, 27):
		number = count
		# Split the list into draws
		for draw in a_list:
			draw_list = draw.split()
			if int(draw_list[5]) == number:
				counter += 1

		powerballs.append(number)
		powerballs_count.append(counter)
		counter = 0

	for count in range(1, 70):
		number = count
		for draw in a_list:
			draw_list = draw.split()
			draw_list = draw_list[0:5]  # Corrected, values without pbnumbers

			for searchnumber in draw_list:
				if int(searchnumber) == number:
					counter += 1

		non_powerballs.append(number)
		non_powerballs_count.append(counter)
		counter = 0

	# print(non_powerballs_count)

	print('Powerballs Frequency')
	print('--------------------')
	print()
	print('Number\t\tTimes')
	print('------\t\t-----')

	for index in range(len(powerballs)):
		print(str(powerballs[index]) + '\t--->\t' + str(powerballs_count[index]))

	print()
	print('Rregular Frequency')
	print('------------------')
	print()
	print('Number\t\tTimes')
	print('------\t\t-----')

	for index in range(len(non_powerballs)):
		print(str(non_powerballs[index]) + '\t--->\t' + str(non_powerballs_count[index]))

	# print()
	# print()
	# print(a_list)


def main():
	infile = open('pbnumbers.txt', 'r')

	# Read the file and create a list
	contents = infile.readlines()
	for index in range(len(contents)):
		contents[index] = contents[index].rstrip('\n')

	infile.close()
	# print(contents)
	master_list, split_list = unified_list(contents)

	numbersfound, timesfound = times_each_appear(master_list)

	top_ten_common(timesfound, numbersfound)
	bottom_ten_common(timesfound, numbersfound)
	top_10_overdue(timesfound, numbersfound, master_list)
	separate_frequency(contents)
	# print(contents)
	# print()
	# print(master_list)

main()
