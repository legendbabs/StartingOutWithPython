def main():
	distance_km = float(input('Eneter a distance in km: '))

	kilo_converter(distance_km)


def kilo_converter(distance):
	distance_miles = distance * 0.6214
	print(f'{distance}Km is equal to {distance_miles:,.2f}Miles.')

main()