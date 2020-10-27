# This program calculates the area of two rectangles and check
# which has the greatest area and if the areas are the same

length1 = int(input('Enter the length of the first rectangle: '))
width1 = int(input('Enter the width of the first rectangle: '))

length2 = int(input('Enter the length of the second rectangle: '))
width2 = int(input('Enter the width of the second rectangle: '))

area1 = length1 * width1
area2 = length2 * width2

print(area1)
print(area2)
print()

if area1 > area2:
	print('The First Rectangle Has The Largest Area.')
elif area2 > area1:
	print('The Second Rectangle Has The Largest Area.')
else:
	print('Both Rectangles Has Equal Areas.')
