def main():
	list_items = [3, 5, 6, 9, 8, 10, 15, 2, 1, 7]

	largest_list_items(list_items, 0, len(list_items)-1)
	
	

def largest_list_items(items, start, end):
	if end > start:
		if items[start] > items[start+1]:
			del items[start+1]
		else:
			del items[start]
		largest_list_items(items, start, end-1)

	if end == 1:
		# return items[0]
		print('Largest Number Is:', items[0])

main()


