def main():
	infile = open('sales.txt', 'r')
	value = infile.readline()

	while value != '':
		line = float(value)
		print(line)

		value = infile.readline()

	infile.close()

main()

# m = '99'
# print(int(m))
# num = float(m)
# print(num)
# print(str(num))