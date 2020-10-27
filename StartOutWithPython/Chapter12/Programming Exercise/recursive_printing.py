# First method 
def main():
	number = int(input('Enter a number: '))
	recursive_printing(number)


def recursive_printing(n):
	if n > 0:
		print(n)
		recursive_printing(n-1)

main()


# second method
def main():
	number = int(input('Enter a number: '))
	recursive_printing(number, 1)


def recursive_printing(n, start):
	if n > 0:
		print(start)
		start += 1
		recursive_printing(n-1, start)

main()
