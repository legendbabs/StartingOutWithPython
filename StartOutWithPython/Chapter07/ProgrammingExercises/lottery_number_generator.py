# This program is used to simulate a lottery number generator

import random

NUM_LOT = 7

def main():
	# Create a list to store the random numbers
	lottery_list = [0] * NUM_LOT
	
	# Generate random lottery numbers in the range of 0 through 9 and save it to the lottery list
	
	for index in range(NUM_LOT):
		lot_num = random.randint(0, 9)
		lottery_list[index] = lot_num
		
	# Display the contents of the list
	print("Here is the lists of the lottery numbers generated:")
	for rand_num in lottery_list:
		print(rand_num)
		
main()
		