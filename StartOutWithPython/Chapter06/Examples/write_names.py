def main():
	print('Enter the names of three friends.')
	name1 = input('Friend #1: ')
	name2 = input('Friend #2: ')
	name3 = input('Friend #3: ')

	myfile = open('friends.txt', 'w')
	# myfile.write(f'{name1}\n{name2}\n{name3}')
	myfile.write(name1 + '\n')
	myfile.write(name2 + '\n')
	myfile.write(name3 + '\n')

	myfile.close()

	print('The names are written to friends.txt.')

main()