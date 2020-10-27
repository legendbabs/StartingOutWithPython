def main():
	found = False
	coffee_file = open("coffee.txt", "r")
	
	search = input("Enter the description to search for: ")
	
	descr = coffee_file.readline()
	while descr != "":
		qty = float(coffee_file.readline())
		
		descr = descr.rstrip("\n")
		
		if search == descr:
			print("Description:", descr)
			print("Quantity:", qty)
			found = True
			
		descr = coffee_file.readline()
		
	coffee_file.close()
	
	if not found:
		print("The description was not found in the records.")
		
main()
			