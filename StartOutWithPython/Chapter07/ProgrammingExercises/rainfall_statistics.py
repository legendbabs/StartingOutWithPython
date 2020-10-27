# This program calculates and display total rainfall for the year, the average monthly rainfall, months with highest rainfall, months with lowest rainfall

MONTHS_TOT = 12

def main():
	total = 0.0
	
	rainfall_monthly_list = [0] * MONTHS_TOT
	
	for index in range(MONTHS_TOT):
		print("Enter the amount of rainfall for month #", index+1, ": ", sep="", end="")
		amount = float(input())
		rainfall_monthly_list[index] = amount
		
	print()
	# calculate the total rainfall
	for val in rainfall_monthly_list:
		total += val
		
	print("The total annual rainfall is:", format(total, ",.2f"))
	
	print()
	# calculate the average rainfall
	avg = total / MONTHS_TOT
	print("The average monthly rainfall is:", format(avg, ",.2f"))
	
	print()
	# month with maximum rainfall
	max_rainfall = max(rainfall_monthly_list)
	
	# month with minimum rainfall
	min_rainfall = min(rainfall_monthly_list)
	
	print()
	for index in range(MONTHS_TOT):
		if rainfall_monthly_list[index] == max_rainfall:
			print("The month with maximum amount of rainfall is: Month", index+1)
			print("Maximum Rainfall:", max_rainfall)
			print()
		elif rainfall_monthly_list[index] == min_rainfall:
			print("The month with minimum amount of rainfall is: Month", index+1)
			print("Minimum Rainfall:", min_rainfall)
			print()
			
main()
		
		