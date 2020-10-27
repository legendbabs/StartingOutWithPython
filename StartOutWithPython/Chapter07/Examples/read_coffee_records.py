def main():
	coffee_file = open("coffee.txt", "r")
	
	# read the first line
	descr = coffee_file.readline()
	while descr != "":
		qty = float(coffee_file.readline())
		
		# strip the new line using rstrip method
		descr = descr.rstrip("\n")
		
		print("Description:", descr)
		print("Quantity:", qty)
		print()
		
		# read another line
		
		descr = coffee_file.readline()
		
	coffee_file.close()
	
main()