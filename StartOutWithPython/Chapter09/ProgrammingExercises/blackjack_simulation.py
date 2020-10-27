import random

# deck_dict = {
# 'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3, '4 of Hearts': 4, '5 of Hearts': 5, 
# '6 of Hearts': 6, '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9, '10 of Hearts': 10, 
# 'Jack of Hearts': 10, 'Queen of Hearts': 10, 'King of Hearts': 10, 'Ace of Spades': 1, 
# '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6, 
# '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9, '10 of Spades': 10, 'Jack of Spades': 10, 
# 'Queen of Spades': 10, 'King of Spades': 10, 'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3, 
# '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6, '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9, 
# '10 of Clubs': 10, 'Jack of Clubs': 10, 'Queen of Clubs': 10, 'King of Clubs': 10, 'Ace of Diamonds': 1, 
# '2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6, 
# '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9, '10 of Diamonds': 10, 'Jack of Diamonds': 10, 
# 'Queen of Diamonds': 10, 'King of Diamonds': 10
# }

# print(len(deck_dict))

def createdeck():
	# Another method to create the deck dictionary
	value = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
	suit = ('of Hearts', 'of Spades', 'of Clubs', 'of Diamonds')
	deck = dict()
	counter = 1

	for element in suit:
		for item in value:
			deck[item + ' ' + element] = counter
			if counter < 10:
				counter += 1
			else:
				counter = 10
		counter = 1

	return deck


def deal_cards(a_deck):
	player_1_hand = 0
	player_2_hand = 0
	player_1_score = 0
	player_2_score = 0

	for count in range(len(a_deck) // 2):
		card1 = random.choice(list(a_deck.keys()))
		value1 = a_deck[card1]
		del a_deck[card1]
		print(card1)
		if card1.startswith('Ace') and (11 + player_1_hand) < 21:
			value1 = 11
		else:
			value1 = 1
		player_1_hand += value1
		print('Player 1:', player_1_hand)

		card2 = random.choice(list(a_deck.keys()))
		value2 = a_deck[card2]
		del a_deck[card2]
		print(card2)
		if card2.startswith('Ace') and (11 + player_2_hand) < 21:
			value2 = 11
		else:
			value2 = 1
		player_2_hand += value2
		print('Player 2:', player_2_hand)

		if player_1_hand > 21 and player_2_hand > 21:
			print('No one wins')
			player_1_hand = 0
			player_2_hand = 0

		elif player_1_hand > 21 and player_2_hand <= 21:
			print('Player 2 wins')
			player_2_score += 1
			player_1_hand = 0
			player_2_hand = 0

		elif player_2_hand > 21 and player_1_hand <= 21:
			print('Player 1 wins')
			player_1_score += 1
			player_1_hand = 0
			player_2_hand = 0

		else:
			print('Round continues')

	print('Player 1', player_1_score)
	print('Player 2', player_2_score)

	if player_1_score > player_2_score:
		print('Player 1 wins!')
	elif player_2_score > player_1_score:
		print('Player 2 wins!')
	else:
		print('It is a TIE!')


def main():
	deck = createdeck()
	deal_cards(deck)

main()