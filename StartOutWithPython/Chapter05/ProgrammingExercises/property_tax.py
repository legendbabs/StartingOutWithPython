
# This program displays the property tax and assessment value
# on a piece of land

MULTIPLIER = 0.6
ASS_MULTIPLIER = 10000
PROP_MULTIPLIER = 72

def property_tax():
	actual_val = float(input('Enter the property actual value: '))

	assessment_val = actual_val * MULTIPLIER

	# For each $100 of the assessment value
	# assessment value / 100

	each_assess_val = assessment_val / ASS_MULTIPLIER
	property_tax = each_assess_val * PROP_MULTIPLIER

	print(f'The Assessment Value Is: ${assessment_val:,.2f}')
	print(f'The Property Tax Is: ${property_tax:,.2f}')

property_tax()