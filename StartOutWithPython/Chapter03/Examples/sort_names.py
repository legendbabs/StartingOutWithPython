# This program compares string with the less than (<) operator

name1 = input('Enter a name (last name first): ')
name2 = input('Enter another name (last name first): ')

print('Here are the names listed in alphabetical order...')
print()

if name1 < name2:
	print(name1)
	print(name2)

else:
	print(name2)
	print(name1)