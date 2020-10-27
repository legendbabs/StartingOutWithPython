# This program demonstrates varoius set operations.
baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

# Display numbers of the baseball set.
print('The following students are on the baseball team: ')
for name in baseball:
	print(name)

print()

# Display numbers of the basketball set.
print('The following students are on the basketball team: ')
for name in basketball:
	print(name)

print()
# Demonstrates the intersection
print('The following students play both baseball and basketball: ')
for name in baseball.intersection(basketball):
	print(name)

print()
# Demonstrate union
print('The following students play either baseball or basketball: ')
for name in baseball.union(basketball):
	print(name)

print()
# Demonstarate the difference of baseball and basketball
print('The following students play baseball, but not basketball: ')
for name in baseball.difference(basketball):
	print(name)

print()
# Demonstarate the difference of basketball and baseball
print('The following students play basketball , but not baseball: ')
for name in basketball.difference(baseball):
	print(name)

print()
# Demonstarate the symmetric difference 
print('The following students play one sport, but not both: ')
for name in baseball.symmetric_difference(basketball):
	print(name)


