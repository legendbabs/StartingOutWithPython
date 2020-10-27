# This program checks the grade of student and displays it on the screen

A_GRADE = 90
B_GRADE = 80
C_GRADE = 70
D_GRADE = 60

student_score = int(input('Enter your score to check your grade: '))

if student_score >= A_GRADE:
	print('Your Grade = A.')
elif student_score >= B_GRADE and student_score < A_GRADE:
	print('Your Grade = B.')
elif student_score >= C_GRADE and student_score < B_GRADE:
	print('Your Grade = C.')
elif student_score >= D_GRADE and student_score < C_GRADE:
	print('Your Grade = D.')
else:
	print('Your Grade is F.')
