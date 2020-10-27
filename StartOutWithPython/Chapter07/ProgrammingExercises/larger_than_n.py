def main():
	
	# This is the list
	numbers_list = list_func()
	print()
	
	# Enter a number n
	n = int(input("Enter a number (n) to compare with larger numbers in the list: "))
	
	# This is the list of numbers greater than n
	larger_list = larger_than_n(n, numbers_list)
	
	# Display the numbers
	print("The numbers that are larger than", n, "are:")
	counter = 1
	for n_each in larger_list:
		print(n_each, end="")
		if counter < len(larger_list):
			print(end=", ")
			counter += 1
	

def list_func():
	num_list = []
	again = "y"
	while again == "y":
		print("Enter a number to add to the list: ", end="")
		num = int(input())
		num_list.append(num)
		
		again = input("Add more numbers? [Y/n] to continue: ")
		
	return num_list
	
def larger_than_n(num, n_list):
	count_large = []
	for number in n_list:
		if number > num:
			count_large.append(number)
			
	return count_large
			
	print()
	
main()
		
		