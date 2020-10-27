def main():
	outfile = open("charge_accounts.txt", "w")
	again = "y"
	while again == "y" or again == "Y":
		print("Enter a (7 digits) account number:", end="")
		acc = int(input())
		outfile.write(str(acc) + "\n")
		
		print("Add more Account  Numbers? [Y/n]: ", end="")
		again = input()
		
	outfile.close()
	
	print("Account Numbers has been written to charge_accounts.txt.")
	
main()
		