# First method with the main function
def main():
	number = int(input('Enter a number: '))
	recursive_line(number, 1)

def recursive_line(n, start):
	if n > 0:
		print('*' * start)
		start += 1
		recursive_line(n-1, start)

main()


# Second Method Without the main function
number = int(input('Enter a number: '))
def recursive_line(n, start):
	if n > 0:
		print('*' * start)
		start += 1
		recursive_line(n-1, start)

recursive_line(number, 1)