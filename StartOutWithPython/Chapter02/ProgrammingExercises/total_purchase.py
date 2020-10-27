TAX = 0.07
total_sales = 0.0
sub_total = 0.0
total_tax = 0.0


for item in range(5):
	print('Enter the price of item #', item+1, end='')
	price = float(input(': '))
	sales_tax = TAX * price
	sale = price - sales_tax
	sub_total += sale
	total_tax += sales_tax
	total_sales += sale
	print(f'Subtotal: {sub_total}')
	print()
	print(f'Total Tax: {total_tax}')

print(f'Total Sales: ${total_sales}')