def main():
	outfile = open('1994_Weekly_Gas_Averages.txt', 'w')
	for i in range(52):
		price = int(input('Gas Price for day #' + str(i+1) + ': '))
		outfile.write(str(price) + '\n')

	outfile.close()

	print('Gas price has been written to 1994_Weekly_Gas_Averages.txt.')

main()