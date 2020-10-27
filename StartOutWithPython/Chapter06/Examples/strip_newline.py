def main():
	infile = open('friends.txt', 'r')

	name1 = infile.readline()
	name2 = infile.readline()
	name3 = infile.readline()

	name1 = name1.rstrip('\n')
	name2 = name2.rstrip('\n')
	name3 = name3.rstrip('\n')

	infile.close()

	print(name1)
	print(name2)
	print(name3)

main()