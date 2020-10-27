def main():
	write_file()
	read_words()
	
def write_file():
	outfile = open("words.txt", "w")
	
	user_str = input("Enter some words: ")
	outfile.write(user_str)
	outfile.close()
	
	
def read_words():
	count_words = 1
	dict_words = {}
	found = False
	
	infile = open("words.txt", "r")
	content = infile.read()
	infile.close()
#	print(content)
	
	word_split = content.split()
	print(word_split)
	print()
	
	for item in word_split:
		if item == ',':
			continue
		elif item == '-':
			continue
		elif item not in dict_words:
			dict_words[item] = count_words
		else:
			found = True
			count_words = dict_words[item] + 1
			dict_words[item] = count_words
			
		count_words = 1 
					
	print()
	print('Word\tFrequency')
	print('------------------')
	for word, freq in dict_words.items():
		print(word + '\t\t' + str(freq))
				
#		print(item)
#	print(word_split)
	
#	set_word = set(word_split)
#	print(set_word)
	
main()