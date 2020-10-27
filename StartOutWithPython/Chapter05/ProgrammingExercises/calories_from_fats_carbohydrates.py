# This program asks the user to enter the number of 
# fats gram and carbohydrates gram consume per day
# and displays their calories on screen.

def main():
	fat_gram = float(input('Enter the number of fat grams consumed per day: '))
	carbohydrates_gram = float(input('Enter the number of carbohydrates grams consumed per day: '))

	calories_from_fats = fatty(fat_gram)
	calories_from_carbohydrates = carbo(carbohydrates_gram)

	print(f'Calories From Fats Is: {calories_from_fats}Kcal')
	print(f'Calories From Carbohydrates Is: {calories_from_carbohydrates}Kcal')



def fatty(fat):
	calories = fat * 9
	return calories


def carbo(car):
	calories = car * 4
	return calories


main()