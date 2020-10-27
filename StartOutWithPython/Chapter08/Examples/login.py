# Define a get login  function with first name, last name
# and id number characters

def get_login_name(first, last, idnumber):
	set1 = first[0:3]
	set2 = last[0:3]
	set3 = idnumber[-3:]

	# Concatenate the  three datas
	login_name = set1 + set2 + set3

	return login_name


def validate_password(password):
	has_correct_length = False
	has_uppercase = False
	has_lowercase = False
	has_digit = False

	if len(password) >= 7:
		has_correct_length = True

		for ch in password:
			if ch.isupper():
				has_uppercase = True
			if ch.islower():
				has_lowercase = True
			if ch.isdigit():
				has_digit = True

	if has_correct_length and has_uppercase and has_lowercase and has_digit:
		is_valid = True
	else:
		is_valid = False
	return is_valid
