MIN = 1950
MAX = 1990

def main():
	total = 0
	infile = open("USPopulation.txt", "r")
	pop_list = infile.readlines()
	
	for index in range(len(pop_list)):
		pop_list[index] = int(pop_list[index])
		
	#print()
	for pop in pop_list:
		total += pop
		
	avg_pop = total / len(pop_list)
	max_pop = max(pop_list)
	min_pop = min(pop_list)
	
	print("Total Annual Population Is: ", format(total, ",.1f"))
	
	print("Average Yearly Population Is: ", format(avg_pop, ",.1f"), sep="")
	
	index = 1950
	for count in range(len(pop_list)):
		if pop_list[count] == max_pop:
			print("The year with greatest increase in population is:", index)
		elif pop_list[count] == min_pop:
			print("The year with lowest increase in population is:", index)
		index += 1
		
main()
		
	
	
	
	