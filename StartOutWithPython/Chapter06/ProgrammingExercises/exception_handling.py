# This program modifies the program written in average_of_numbers.py module
# and should handle the following errors... IOError when reading files 
# and ValueError when items read are converted to numbers

def main():
	total = 0.0
	count = 0

	
	try:
		infile = open('numbers.txt', 'r')

		for line in infile:
			val = float(line)
			count += 1
			total += val

		infile.close()

		average = total / count

		print(f'The average of all numbers in the file (numbers.txt) is {average:.1f}.')

	# handling FileNotFoundError
	except IOError:
		print('The data can not be read from the file.')

	# handling bad data error
	except ValueError:
		print('The value cnnot be converted to numbers.')

main()