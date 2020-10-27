# This program asks the user to enter sales amount for a month
# and save them in a file name sales_data.txt

def main():
	again = 'y'
	sales_file = open('sales_data.txt', 'w')

	while again == 'y' or again == 'Y':
		print('Enter the sales amount for a month', end='')
		sales = float(input(': '))

		sales_file.write(str(sales) + '\n')

		again = input('Do you want to enter more sales? [Y/n] to continue: ')

	sales_file.close()

	print('Sales has been written to sales_data.txt.')

main()