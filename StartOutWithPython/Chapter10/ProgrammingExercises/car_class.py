class Car:
	def __init__(self, year_model, make, speed):
		self.__year_model = year_model
		self.__make = make
		self.__speed = speed

	def set_year_model(self, year_model):
		self.__year_model = year_model

	def set_make(self, make):
		self.__make = make

	def get_year_model(self):
		return self.__year_model

	def get_make(self):
		return self.__make

	def set_speed(self, speed):
		self.__speed = speed

	def accelerate(self):
		self.__speed += 5
	
	def brake(self):
		self.__speed -= 5

	def get_speed(self):
		return self.__speed


def main():
	# Create the car object name my_car
	my_car = Car(2003, 'BMW', 100)

	# Set the curent speed to 0
	my_car.set_speed(0)

	# Call the accelerate method 5 times
	for i in range(5):
		my_car.accelerate()
		print('Current Speed Of the Car:', my_car.get_speed())
	print()

	# Call the brake method 5 times
	for j in range(5):
		my_car.brake()
		print('Current Speed Of the Car:', my_car.get_speed())

main()




