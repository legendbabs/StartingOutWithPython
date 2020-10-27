import matplotlib.pyplot as plt

def main():
	left_edges = [0, 10, 20, 30, 40]
	heights = [100, 200, 300, 400, 500]
	bar_widths = 10
	
	plt.bar(left_edges, heights, bar_widths, color=("r", "b", "y", "g", "k"))
	
	plt.title("Sales By Year")
	plt.xlabel("Year")
	plt.ylabel("Sales")
	plt.xticks([5, 15, 25, 35, 45], ["2016", "2017", "2018", "2019", "2020"])
	
	plt.yticks([0, 100, 200, 300, 400, 500], ["$0m", "$1m", "$2m", "$3m", "$4m", "$5m"])
	plt.show()
	
main()