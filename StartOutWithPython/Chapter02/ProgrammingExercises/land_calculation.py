one_acre = 43560 # sq feet

land_sqfeet = float(input('Enter the land\'s square feet: '))
num_acres = land_sqfeet / one_acre
print('The number of acres in the land is ',format(num_acres, '.2f'), 'acres')
