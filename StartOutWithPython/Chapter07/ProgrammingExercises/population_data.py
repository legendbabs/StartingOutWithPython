import random

MIN = 1950
MAX = 1990

def main():
	
	outfile = open("population.txt", "w")
	
	for index in range(MIN, MAX+1):
		num_pop = random.randint(150000, 350000)
		outfile.write(str(num_pop) + "\n")
		
	outfile.close()
	print("Populations number has been written to population.txt.")
	
main()
	