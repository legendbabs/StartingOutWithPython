# This program displays the celsius and their fahrenheit equivalents

LIMIT = 20
print('Celsius\tFarhenheit')

for C in range(1, LIMIT+1):
	F = 95 / (C + 32)
	print(C, '\t', format(F, '.1f'))
