def main():
	user_input = input('Enter a string: ')

	vow = vowels_funct(user_input)
	cons = consonants_funct(user_input)

	# Display the result

	print('Total vowel letters is:', vow)
	print('Total consonants letters is:', cons)


def vowels_funct(user_input):
	count_vow = 0
	vowels_alph = 'aeiou'

	for ch in user_input:
		if ch in vowels_alph:
			count_vow += 1

	return count_vow


def consonants_funct(user_input):
	count_cons = 0
	consonants_alph = 'bcdfghjklmnpqrstvwxyz'

	for ch in user_input:
		if ch in consonants_alph:
			count_cons += 1

	return count_cons

main()
