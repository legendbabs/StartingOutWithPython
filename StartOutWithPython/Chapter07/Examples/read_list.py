# this program reads a file's contents into a list

def  main():
	infile = open('cities.txt', 'r')

	# read the contents of the file into a list
	cities = infile.readlines()

	infile.close()

	# strip the newline from each elements
	# index = 0
	# while index < len(cities):
	# 	cities[index] = cities[index].rstrip('\n')
	# 	index += 1

	print(cities)

main()