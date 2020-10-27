def get_textname():
	name = input('For which file would you like to create a word index: ')
	return name


def create_dictionary(filename):
	infile = open(filename, 'r')
	word_index = dict()
	counter = 0
	for line in infile:
		wordline_list = line.rstrip('\n').split()
		counter += 1
		for word in wordline_list:
			if word not in word_index:
				word_index[word] = [str(counter)]
			elif word in word_index:
				word_index[word].append(str(counter))

	infile.close()
	return word_index
	# print(word_index)


def create_indexfile(dict):
	outfile = open('index.txt', 'w')
	a_list = []
	index = 0
	for key in dict.keys():
		a_list.append(key)
		for value in dict[key]:
			a_list[index] = a_list[index] + ' ' + value
		index += 1
	a_list.sort()

	for element in a_list:
		outfile.write(element + '\n')
	outfile.close()


def main():
	print('This program creates a word index of the file you request:')
	print('----------------------------------------------------------')
	print()
	file = get_textname()
	dictionary = create_dictionary(file)
	create_indexfile(dictionary)



main()