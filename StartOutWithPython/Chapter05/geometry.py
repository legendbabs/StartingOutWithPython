import circle
import rectangle

AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

def main():
	choice = 0
	while choice != QUIT_CHOICE:
		display_menu()

		choice = int(input('Enter your choice: '))
		if choice == AREA_CIRCLE_CHOICE:
			radius = float(input('Enter the circle\'s radius: '))
			print('The Area is', circle.area(radius))
		elif choice == CIRCUMFERENCE_CHOICE:
			radius = float(input('Enter the circle\'s radius: '))
			print('The Circumference is', circle.circumference(radius))
		elif choice == AREA_RECTANGLE_CHOICE:
			width = float(input('Enter the rectangle\'s width: '))
			length = float(input('Enter the rectangle\'s length: '))
			print('The Area of the rectangle is', rectangle.area(width, length))
		elif choice == PERIMETER_RECTANGLE_CHOICE:
			width = float(input('Enter the rectangle\'s width: '))
			length = float(input('Enter the rectangle\'s length: '))
			print('The Perimeter of is', rectangle.perimeter(width, length))
		elif choice == QUIT_CHOICE:
			print('Exiting the program...')
		else:
			print('Error: Invalid Selection.')


def display_menu():
	print('MENU')
	print('1) Area of a circle')
	print('2) Circumference of a circle')
	print('3) Area of a Rectangle')
	print('4) Perimeter of a Rectangle')
	print('5) Quit')


main()



