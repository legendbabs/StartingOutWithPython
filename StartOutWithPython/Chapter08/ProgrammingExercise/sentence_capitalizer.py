def main():
	user_str = input('Enter a string to convert: ')
	split_str = user_str.split()

	for item in split_str:
		res = perf_funct(item)
		print(res, end='')


def perf_funct(split_word):
	set1 = split_word[0].upper()
	set2 = split_word[1:] + ' '
	return set1 + set2

main()


# Shina's code
# def main():
#     # Ask user to enter a sentence
#     word = input('Please enter a sentence: ') 
#     print(sentence(word))
    
# def sentence(word):
#     first = word[0].upper()
#     last = word[1:]
#     upper_word = first + last
#     return upper_word

# main()
