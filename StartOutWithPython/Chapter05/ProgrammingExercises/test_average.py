def main():
	score_1 = int(input('Enter the first score: '))
	score_2 = int(input('Enter the second score: '))
	score_3 = int(input('Enter the third score: '))
	score_4 = int(input('Enter the fourth score: '))
	score_5 = int(input('Enter the fifth score: '))

	average = calc_average(score_1, score_2, score_3, score_4, score_5)

	for score in range(1, 6):
		if score == 1:
			first_grade = determine_grade(score_1)
		elif score == 2:
			second_grade = determine_grade(score_2)
		elif score == 3:
			third_grade = determine_grade(score_3)
		elif score == 4:
			fourth_grade = determine_grade(score_4)
		else:
			fifth_grade = determine_grade(score_5)

	print()
	print('Test\tScore\tGrade')
	print('=====================')
	print('Test1\t', score_1, '\t', first_grade)
	print('Test2\t', score_2, '\t', second_grade)
	print('Test1\t', score_3, '\t', third_grade)
	print('Test1\t', score_4, '\t', fourth_grade)
	print('Test1\t', score_5, '\t', fifth_grade)

	print()
	print('The average score is:', format(average, '.1f'))



def calc_average(score_1, score_2, score_3, score_4, score_5):
	avg = (score_1 + score_2 + score_3 + score_4 + score_5) / 5
	return avg


def determine_grade(score):
	if score >= 90 and score <= 100:
		return 'A'
	elif score >= 80 and score < 90:
		return 'B'
	elif score >= 70 and score < 80:
		return 'C'
	elif score >= 60 and score < 70:
		return 'D'
	elif score <= 60:
		return 'F'
	else:
		return 'Invalid Score !!!'


main()