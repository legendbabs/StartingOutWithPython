

def main():
	infile = open('text.txt', 'r')
	text = infile.read()
	infile.close()
	# print(text)

	str_text(text)
	print('Total Letters:', len(text))


def str_text(read_text):
	count_upper = 0
	count_lower = 0
	count_digit = 0
	count_space = 0

	for ch in read_text:
		if ch.isupper():
			count_upper += 1
		elif ch.islower():
			count_lower += 1
		elif ch.isdigit():
			count_digit += 1
		elif ch.isspace():
			count_space += 1
	print('Uppercase Letters:', count_upper)
	print('Lowercase Letters:', count_lower)
	print('Digits:', count_digit)
	print('Space:', count_space) 

	total_letters = count_upper + count_lower
	# print('Total Letters 2nd Method:', total_letters)

	print()


main()