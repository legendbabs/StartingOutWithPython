def main():
	encryption_dataset, decryption_dataset = encryption_rules()
	filename = input('Enter a txt file name: ')
	print()
	choice = int(input('Press (1) to encrypt, OR (2) to decrypt: '))
	if choice == 1:
		encrypt(filename, encryption_dataset)
	elif choice == 2:
		decrypt(filename, decryption_dataset)
	else:
		print('Not a valid choice.')


def encryption_rules():
	encryption_dataset = dict()
	decryption_dataset = dict()
	characters = "!@#$%^&*()_+~`1234567890-={[}]:;>.<,?/AaBbCcFfRrDdTtGgYyHhJjUuKkOoLlp"
	letters = """AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz 1234567890’'"-.,"""

	for index in range(len(letters)):
		encryption_dataset[letters[index]] = characters[index]
		decryption_dataset[characters[index]] = letters[index]

	return encryption_dataset, decryption_dataset
	# print(len(characters))
	# print(len(letters))


def encrypt(a_file, encryption_rules):
	infile = open(a_file, 'r')
	outfile = open('encrypted_' + a_file, 'w')
	text = []
	encrypted_text = []

	for line in infile:
		text.append(line.rstrip('\n'))

	for line in text:
		encrypted_line = ''
		for char in line:
			encrypted_line += encryption_rules.get(char, '')
		encrypted_text.append(encrypted_line)

	for line in encrypted_text:
		outfile.write(line + '\n')

	infile.close()
	outfile.close()


def decrypt(a_file, decryption_rules):
	infile = open('encrypted_' + a_file, 'r')
	outfile = open('decrypted_' + a_file, 'w')

	encrypted_text = []
	decrypted_text = []

	for line in infile:
		encrypted_text.append(line.rstrip('\n'))

	for line in encrypted_text:
		decrypted_line = ''
		for char in line:
			decrypted_line += decryption_rules.get(char, '')
		decrypted_text.append(decrypted_line)

	for line in decrypted_text:
		outfile.write(line + '\n')

	infile.close()
	outfile.close()


main()