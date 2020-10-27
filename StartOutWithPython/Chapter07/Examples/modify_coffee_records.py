import os

def main():
	found = False
	coffee_file = open("coffee.txt", "r")
	temp_file = open("temp.txt", "w")
	
	search = input("Enter the description to search for: ")
	new_qty = int(input("Enter the new quantity (in pounds): "))
	
	descr = coffee_file.readline()
	while descr != "":
		qty = float(coffee_file.readline())
		
		descr = descr.rstrip("\n")
		
		if search == descr:
			temp_file.write(descr + "\n")
			temp_file.write(str(new_qty) + "\n")
			found = True
			
		else:
			temp_file.write(descr + "\n")
			temp_file.write(str(qty) + "\n")
			
		descr = coffee_file.readline()
		
	coffee_file.close()
	
	os.remove("coffee.txt")
	os.rename("temp.txt", "coffee.txt")
	
	if found:
		print("The coffee record has been updated..")
	else:
		print("The description was not found in the list.")
		
main()