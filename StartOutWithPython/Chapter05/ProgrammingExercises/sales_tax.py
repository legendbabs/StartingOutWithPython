# This program ask the user to enter the amount of purchase
# Then compute the state and county sales tax

STATE_SALES_TAX = 0.05
COUNTY_SALES_TAX = 0.025

def main():
	purchase_price = purchase_amount()

	state_price = state_sales(purchase_price)

	county_price = county_sales(purchase_price)

	total_sales = total_sales_tax(state_price, county_price)

	print(f'Puchased Amount Is: ${purchase_price:,.2f}')
	print(f'The State Sales Tax Is: ${state_price:,.2f}')
	print(f'The County Sales Tax Is: ${county_price:,.2f}')
	print(f'The Total Sales Is: ${total_sales:,.2f}')


def purchase_amount():
	purchase = float(input('Enter the amount of purchase: '))
	return purchase


def state_sales(price):
	state_sales_price = price * STATE_SALES_TAX
	return state_sales_price


def county_sales(price):
	county_sales_price = price * COUNTY_SALES_TAX
	return county_sales_price


def total_sales_tax(state, county):
	return state + county

main()
