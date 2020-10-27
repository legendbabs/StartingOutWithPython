PROFIT = 0.23
total_sales = float(input('Enter the total sales: '))
gain = PROFIT * total_sales
annual_profit = total_sales + gain
print('The annual profit is $', format(annual_profit, ',.2f'), sep='')
