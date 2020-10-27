#print("hello world")
def main():
	found = False
	
	infile = open("charge_accounts.txt", "r")
	charge_account = infile.readlines()
	
	index = 0
	while index < len(charge_account):
		charge_account[index] = int(charge_account[index])
		index += 1
		
	infile.close()
#	print(charge_account)
	print()
		
	search = int(input("Enter an account number to search for in the list: "))
	
	for account in charge_account:
		if account == search:
			found = True
			
	if found:
		print(search, "is a valid account number.")
	else:
		print(search, "is an invalid account number.")
			
main()