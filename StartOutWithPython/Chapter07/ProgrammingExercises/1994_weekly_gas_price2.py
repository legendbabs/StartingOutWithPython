import matplotlib.pyplot as plt 


def main():
	infile = open('1994_Weekly_Gas_Averages.txt', 'r')
	gas_price = infile.readlines()

	for index in range(len(gas_price)):
		gas_price[index] = int(gas_price[index])

	print()
	left_edges = gas_price
	
	height = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 300, 400, 50, 60, 70, 90, 
	100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 50, 90, 100, 150, 170, 190, 220, 240, 260, 280 ,320, 360, 390, 420, 300]

	bar_width = 5

	plt.xlim(xmin=500, xmax=5000)
	plt.ylim(ymin=10, ymax=1000)

	plt.bar(left_edges, height, bar_width)
	plt.show()

main()




