# This program displays the distance a car has traveled in miles

LIMIT = 3
SPEED = 40

speed = float(input('Enter the speed in Miles\\Hour: '))
hour = int(input('How many hours has the car taken: '))

print('Hour\tDistance Traveled')
print('=========================')

for hr in range(1, hour+1):
	distance = hr * SPEED
	print(f'{hr}\t{distance}')




