import math

# def main():
# 	number = float(input('Enter a number: '))
# 	square_root = math.sqrt(number)
# 	print(f'The Square root of {number} is square_root.')

# main()

# def main():
# 	a = float(input('Enter the length of side A: '))
# 	b = float(input('Enter the length of side B: '))

# 	c = math.hypot(a, b)

# 	print('The length of the hypotenus is', c)

# main()


radius = int(input('Enter the radius of the circle: '))
def area(rad):
	return math.pi * radius ** 2

print('The area is:', format(area(radius),'.1f')) 

def circumference(rad):
	return 2 * math.pi * radius

print('The circumference is:', format(circumference(radius),'.1f')) 
