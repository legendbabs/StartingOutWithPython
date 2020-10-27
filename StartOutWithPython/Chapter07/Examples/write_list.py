def main():
	cities = ['New York', 'Hoston', 'Atlanta', 'Dallas']

	outfile = open('cities.txt', 'w')

	# Write the list to the file
	for item in cities:
		outfile.write(item + '\n')

	outfile.close()

main()