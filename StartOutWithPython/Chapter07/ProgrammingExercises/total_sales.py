# This program asks the user to enter amount of a store's sale for each day of the week, and stored in a list

NUM_WEEK_DAYS = 7

def main():
	total = 0.0
	
	# create a list for sales
	sales_list = [0] * NUM_WEEK_DAYS
	
	# Enter amount of sales
	for index in range(NUM_WEEK_DAYS):
		print("Enter sales for day #", index+1, ": ", sep="", end="")
		sales_list[index] = float(input())
		
	print()
	# Calculate the total sales
	for sale in sales_list:
		total += sale
		
	print(f"Total Sales For The Week Is: ${total:,.2f}.")
	
# call the main function
main()
	
	