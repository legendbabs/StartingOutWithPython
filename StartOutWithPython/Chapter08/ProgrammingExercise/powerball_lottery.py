# import random

# # This program writes random numbers to a file
# def main():
# 	# Open mypbnumbers.txt
# 	outfile = open('mypbnumbers.txt', 'w')
# 	for n in range(109):
# 		pb_num = random.randint(1, 26)
# 		for pb in range(6):
# 			num = random.randint(1, 69)
# 			if pb != 5:
# 				outfile.write(str(num) + ' ')
# 			else:
# 				outfile.write(str(pb_num) + '\n')

# 	outfile.close()

# main()


def main():
	most_num, most_pb, num1 = get_number_list()
	least_num, least_pb, num2 = get_number_list()
	most_over, pb_over, num3 = get_number_list()
	num_freq, pb_freq, num4 = get_number_list()

	print('The most 10 common numbers are: ')

	print(most_common_number(most_num))

	print('The least 10 common numbers are: ')
	print(least_common_number(most_num))

	print('The 10 most overdue numbers are: ')
	print(most_overdue_numbers(most_over))

	# Number frequencies
	print(frequency(num4))
	print()
	print()

	# Pb frequencies
	print(frequency(pb_freq))


def get_number_list():
	infile = open('mypbnumbers.txt', 'r')

	new_list = []
	pb_numbers = []
	numbers = []
	num = []

	for item in infile:
		# print(item)
		ph = item.split()
		# print(ph)
		new_list.append(ph)

	infile.close()
	# print(new_list)
	# print(len(new_list))

	for r in range(len(new_list)):
		for c in range(6):
			numbers.append(new_list[r][c])
			if c != 5:
				num.append(new_list[r][c])

		pb_numbers.append(new_list[r][-1])

	# print(pb_numbers)
	# print()
	# print(numbers)
	# print()
	# print(num)

	return numbers, pb_numbers, num


def most_common_number(numbers):
	counter = 0
	# set function returns a dictionary and removes all duplictes
	# So we have to convert back to list with a list function
	new = list(set(numbers))
	count_list = []
	new_list = []

	for item in new:
		count = numbers.count(item)
		count_list.append(count)

	maxx = list(set(count_list))
	for i in range(-10, 0):
		max_num = sorted(maxx)[i]
		index = count_list.index(max_num)
		index_new = new[index]
		new_list.append(index_new)

	new_list.reverse()

	return new_list


def least_common_number(numbers):
	counter = 0
	new = list(set(numbers))
	count_list = []
	new_list = []

	for item in new:
		count = numbers.count(item)
		count_list.append(count)

	maxx = list(set(count_list))
	for i in range(10):
		max_num = sorted(maxx)[i]
		index = count_list.index(max_num)
		index_new = new[index]
		new_list.append(index_new)

	return new_list


def most_overdue_numbers(numbers):
	new_list = []
	for i in range(-10, 0):
		max_num = numbers[i]
		new_list.append(max_num)

	new_list.reverse()
	return new_list


def frequency(numbers):
	new = list(set(numbers))

	count_list = []
	new_list = []
	for item in new:
		count = numbers.count(item)
		count_list.append(count)

	print('number\tfrequecy')
	for index in range(len(new)):
		print(new[index], '\t', count_list[index])

main()


