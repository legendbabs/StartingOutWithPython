def main():
	user_str = input('Enter a sting: ')

	# set1 = user_str[0]
	# set2 = user_str[1:]


	for char in user_str:
		res = get_set(char)
		print(res, end='')


def get_set(user):
	
	for ch in user:
		if user[0] == ch.upper():
			val = ch

		elif ch.isupper():
			val = user[0] + ' ' + ch.lower() 
		else:
			val = ch

		return val

main()

