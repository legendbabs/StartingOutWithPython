def main():
	number = int(input("Enter a number: "))
	prime = is_prime(number)
	if prime:
		print(number, "is a prime number.")
	else:
		print(number, "is not a prime number.")
	
def is_prime(num):
	counter = 0
	for n in range(2, num):
		if num % n == 0:
			counter += 1
			
	if counter == 0:
		return True
	else:
		return False
			
main()