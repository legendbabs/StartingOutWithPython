# This program calculates the average score of students
# that took three tests and congratulate them if the average
# is greater than 95

HIGH_SCORE = 95

print('Calculate Your average test score: ')
print('----------------------------------')
print()

test1 = float(input('Enter your first test score: '))
test2 = float(input('Enter your second test score: '))
test3 = float(input('Enter your third test score: '))
print()

average_score = (test1+test2+test3) / 3
print(f'Your average score is {average_score:.1f}')

if average_score >= HIGH_SCORE:
	print('Congratulations!!!.')
	print('Great average score...')
