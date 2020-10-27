def main():
	infile = open('philosophers.txt', 'r')
	line1 = infile.readline()
	line2 = infile.readline()
	line3 = infile.readline()
	infile.close()

	print(line1)
	print(line2)
	print(line3)

main()