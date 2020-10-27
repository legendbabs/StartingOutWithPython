# This program reads the contents of two text files
# And compares them in the following ways
# 1) Display a list of all unique words contained in both files
# 2) Display a list of all the words that appears in both files
# 3) Display a list of words that appears in the first file but not in second
# 4) Display a list of words that appears in the second file but not in first
# 4) Display a list of words that appears in either the first file or second file but not both

def main():
	# Create two output files and write words to them
	outfile1 = open('file1.txt', 'w')
	outfile2 = open('file2.txt', 'w')

	word1 = input('Enter the first word: ')
	word2 = input('Enter the second word: ')

	outfile1.write(word1)
	outfile2.write(word2)

	outfile1.close()
	outfile2.close()


	unique_list1, unique_list2 = set_compare()
	# All unique word in first file
	print('All unique words in first file:')
	for word in unique_list1:
		print(word)
	print()

	# All unique word in second file
	print('All unique words in second file:')
	for word in unique_list2:
		print(word)
	print()

	# All the unique words that appear in both files (intersection set)
	print('List of all unique words that appear in both files:')
	for word in unique_list1.intersection(unique_list2):
		print(word)
	print()


	# All the words that appear in both files (union set)
	print('List of all the words that appear in both files:')
	for word in unique_list1.union(unique_list2):
		print(word)
	print()

	# list of words that appears in the first file but not in second(difference set)
	print('Lists of words that appears in the first file but not in second:')
	for word in unique_list1.difference(unique_list2):
		print(word)
	print()

	# list of words that appears in the second file but not in first(difference set)
	print('Lists of words that appears in the second file but not in first:')
	for word in unique_list2.difference(unique_list1):
		print(word)
	print()

	# list of words that appears in either the first file or second file but not both(symmetric differene set)
	print('list of words that appears in either the first file or second file but not both:')
	for word in unique_list1.symmetric_difference(unique_list2):
		print(word)
	print()
	
	
def set_compare():
	# Read the content of the two files

	infile1 = open('file1.txt', 'r')
	infile2 = open('file2.txt', 'r')

	word1 = infile1.read()
	word2 = infile2.read()

	word1_split = (word1.split())
	word2_split = (word2.split())

	# Unique List
	word1_set = set(word1_split)
	word2_set = set(word2_split)

	infile1.close()
	infile2.close()

	# print(word1_split)
	return word1_set, word2_set

main()

