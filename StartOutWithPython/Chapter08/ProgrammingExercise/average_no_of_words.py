def main():
	infile = open('text.txt', 'r')
	text_list = infile.readlines()

	for index in range(len(text_list)):
		text_list[index] = text_list[index].rstrip('\n')

	# print(text_list)

	item_length = []

	for items in text_list:
		count_s = perf_funct(items)
		item_length.append(count_s)

	# This is the list of the lengths of all words
	# print(item_length)
	total = 0
	for str_num in item_length:
		total += int(str_num)
	print('Total Number of words:', total)

	avg = total / len(item_length)
	print('Average Number of words:', avg)

	# Calculate the average word

	# print(text_list[2].split())

def perf_funct(items):
	count = 0
	split_text = items.split()
	for item in split_text:
		count += 1
	return count


main()