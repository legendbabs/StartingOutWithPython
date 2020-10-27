# This program reads player's name and score in a golf amateur club
# as a record with name field and score field in a file named golf.txt

def main():
	# design a mean to control the loop
	again = 'y'

	# open a file named golf.txt in append mode
	golf_file = open('golf.txt', 'a')

	while again == 'y' or again == 'Y':
		player_name = input('Enter the player\'s name: ')
		score = int(input('Enter the player\'s score: '))

		# Write the player's name and score to the golf.txt file
		golf_file.write(player_name + '\n')
		golf_file.write(str(score) + '\n')

		# print a blank space
		print()

		# Enter more player records
		again = input('Enter more player records? [Y/n] to continue: ')

	golf_file.close()

	print('The player\'s records have been written to golf.txt file.')

main()

