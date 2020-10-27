import random

def main():
	infile = open('8_ball_responses.txt', 'r')
	response_list = infile.readlines()

	for index in range(len(response_list)):
		response_list[index] = response_list[index].rstrip('\n')

	print()
	again = 'y'
	while again == 'y' or again == 'Y':
		print('Ask your question and get an answer', end='')

		qst = input(': ')
		print(response_list[random.randint(0, len(response_list)-1)])

		print()
		print('Ask more questions?')
		again = input('[Y/n] to continue: ')

main()
