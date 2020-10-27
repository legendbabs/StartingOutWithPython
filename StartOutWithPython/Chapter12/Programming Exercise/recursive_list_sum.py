# def main():
# 	list_items = [3, 5, 6, 9, 8, 10, 15, 2, 1, 7]

# 	total = recursive_list_sum(list_items, 0, len(list_items)-1)
# 	print('Total Is:', total)

# def recursive_list_sum(items, start, end):
# 	if start > end:
# 		return 0
# 	else:
# 		return items[start] + recursive_list_sum(items, start+1, end)
	

# main()

n = int(input('Enter a number: '))
total = 0

def sum_number(n, total):
    if n > 0:
        total += n
        sum_number(n-1, total)
    if n == 1:
        print(total)
    
sum_number(n, total)



