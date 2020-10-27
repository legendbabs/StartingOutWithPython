import random
def main():
	outfile = open("accounts.txt", "w")
	for index in range(200):
		number = random.randint(5000000, 7000000)
		outfile.write(str(number) + "\n")
		
	outfile.close()
	
main()
	
	