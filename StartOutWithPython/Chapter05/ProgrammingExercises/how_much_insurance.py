INSURANCE_PERCENT = 0.8

def main():
	replacement_cost = float(input('Enter the replacement cost: '))

	insurance_cost = insurance(replacement_cost)
	print(f'Minimum Amount Of Insurance Is: ${insurance_cost:,.2f}')

def insurance(cost):
	insurance_amount = cost * INSURANCE_PERCENT
	return insurance_amount

main()