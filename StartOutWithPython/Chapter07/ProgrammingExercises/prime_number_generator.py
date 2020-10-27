def main():
	number = int(input("Enter a number: "))
	is_prime = prime_numbers(number)
	
	print("Check which of the numbers between 2 and", number, "are (prime) and which are (composites))")
	print(is_prime)
	
	print()
	for index in is_prime:
		res = prime(index)
		
		if res:
			print(index, "is a prime number.")
		else:
			print(index, "is a composite number.")
		

def prime_numbers(number):
	count = 0
	prime_list = []
	for num in range(2, number+1):
		prime_list.append(num)
		
	return prime_list
	

def prime(prime_num):
	count = 0
	for i in range(2, prime_num):
		if prime_num % i == 0:
			count += 1
			
	if count == 0:
		return True
	else:
		return False
	
	
main()
		
	

	
