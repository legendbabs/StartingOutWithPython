total = 0
num_list = []
print("Enter a series of 20 numbers:")
for index in range(20):
	num = int(input("Number #" + str(index+1) + ": "))
	num_list.append(num)
	
min_num = min(num_list)
max_num = max(num_list)

for number in num_list:
	total += number
	
avg = total / len(num_list)

print()
print("The Lowest Number In The List Is:", min_num)
print("The Highest Number In The List Is:", max_num)
print("The Total Of The Numbers In The List Is:", total)
print("The Average Of All The Numbers In The List Is:", avg)