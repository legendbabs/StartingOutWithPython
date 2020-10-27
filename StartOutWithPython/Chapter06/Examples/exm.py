try:
	num1 = int(input('1: '))
	num2 = int(input('2: '))

	result = num1 / num2
	print('Result=', result)

# except ValueError as tunde:
# 	print('Error!!!', tunde)

# except ZeroDivisionError as ibk:
# 	print('Error!!!', ibk)

# To catch all forms of error
except Exception as shina:
	print(shina)