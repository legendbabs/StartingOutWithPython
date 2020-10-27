def main():
	biodata = open('biodata.txt', 'r')
	line1 = biodata.readline()
	line2 = biodata.readline()
	line3 = biodata.readline()
	line4 = biodata.readline()
	line5 = biodata.readline()
	line6 = biodata.readline()
	biodata.close()

	print(line1)
	print(line2)
	print(line3)
	print(line4)
	print(line5)
	print(line6)

main()