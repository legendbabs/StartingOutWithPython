# This program adds as many as coffee records in a file named coffee.txt

def main():
	# open a file coffee.txt in append mode
	coffee_file = open("coffee.txt", "a")
	
	# create a way to controll the loop
	again = "y"
	while again == "y" or again == "Y":
		print("Enter the description of the coffee.")
		descr = input(": ")
		print("Enter the quantity.")
		qty = int(input(": "))
		
		# write the description and the quantity to the file
		coffee_file.write(descr + "\n")
		coffee_file.write(str(qty) + "\n")
		
		# add more coffee records
		again = input("Enter [Y/n] to add more records quit: ")
		
	# close the file
	coffee_file.close()
	print("Coffee records has been written to coffee.txt.")
	
main()