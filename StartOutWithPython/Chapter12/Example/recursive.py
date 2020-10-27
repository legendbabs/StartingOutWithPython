# This program has a recursive function

def main():
	message(5)

def message(times):
	if times > 0:
		print('This is a recursive function.')
		message(times-1)


main()