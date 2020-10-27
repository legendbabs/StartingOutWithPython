# Write a program that asks the user to enter a person’s age. The
# program should display a message indicating whether the person
# is an infant, a child, a teenager, or an adult. 

print('Enter your age to check if you are\nan infant, a child, a teenager, or an adult', end='')
age = int(input(': '))

if age <= 1:
	print('You are an INFANT.')
elif age >= 1 and age < 13:
	print('You are a CHILD.')
elif age >= 13 and age < 20:
	print('You are a TEENAGER.')
elif age >= 20:
	print('You are an ADULT.')
