def main():
	outfile = open('8_ball_responses.txt', 'w')
	for index in range(12):
		response = input('Enter the response #' + str(index+1) + ': ')
		outfile.write(response + '\n')

	outfile.close()

	print('The 12 responses has been written to 8_ball_responses.txt.')

main()
