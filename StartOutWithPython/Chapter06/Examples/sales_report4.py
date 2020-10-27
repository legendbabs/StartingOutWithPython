def main():
	total = 0.0

	try:
		infile = open('sales_data.txt', 'r')
		for line in infile:
			amount = float(line)
			total += amount

		infile.close()

	except Exception as err:
		print(err)

	else:
		print('Total: $', format(total, ',.2f'), sep='')



main()