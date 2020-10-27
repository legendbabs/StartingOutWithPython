def main():
	total = 0.0

	try:
		infile = open('sales_data.txt', 'r')
		for line in infile:
			amount = float(line)
			total += amount

		infile.close()

		print('Total: $', format(total, ',.2f'), sep='')


	# except IOError:
	# 	print('An Error occured trying to read the file.')

	# except ValueError:
	# 	print('Non numeric data found in the file.')

	except:
		print('An error occured.')

main()