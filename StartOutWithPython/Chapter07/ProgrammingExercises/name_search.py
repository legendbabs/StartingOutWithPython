# This program reads the contents of BoyNames.txt and GirlNames.txt
# into a list separately, 

def main():
	# Open a file for bith boys and girls in read mode
	boy_file = open('BoyNames.txt', 'r')
	girl_file = open('GirlNames.txt', 'r')

	# Read the contents of the file to a list
	boys_list = boy_file.readlines()
	girls_list = girl_file.readlines()

	# This is the list of boy names
	boy_names = boy_func(boys_list)

	# This is the list of girls names
	girl_names = girl_func(girls_list)

	user_func(boy_names, girl_names)


def boy_func(boys):
	for index in range(len(boys)):
		boys[index] = boys[index].rstrip('\n')

	return boys


def girl_func(girls):
	for index in range(len(girls)):
		girls[index] = girls[index].rstrip('\n')

	return girls


# Function to perform the operation
def user_func(boy_names, girl_names):
	name = input('Enter a name(Boy name or Girl name): ')
	if name in boy_names or name in girl_names:
		print(name, 'is among the most popular names.')
	else:
		print(name, 'was not found.')


main()
