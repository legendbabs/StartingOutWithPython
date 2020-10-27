import matplotlib.pyplot as plt 

def main():
	expenses = [70000, 25000, 30000, 15000, 120000, 10000]
	categories = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc']
	plt.pie(expenses, labels=categories)
	plt.title('Expense Pie Chart')
	plt.show()

main()