print('How many students wrote the test?', end='')
num_students = int(input(': '))
print('How many subjects was written by each student?', end='')
num_test = int(input(': '))


total_score = []

for student in range(num_students):
	print(f'Student Number #{student+1}')
	print('=================')

	total = 0.0
	for test in range(num_test):
		score = int(input('Enter the score for test number #' + str(test+1) + ': '))
		total += score

	total_score.append(total)
	print()

print(f'Total Score For All The {num_students} is {total_score}')
print()
for index, tot_score in enumerate(total_score):
	avg = tot_score / num_test
	print('Average Score Of Student Number #', index+1, 'is', format(avg, '.1f'))
	# print(f'Average Score Of Student Number #{index+1} is {avg}')
