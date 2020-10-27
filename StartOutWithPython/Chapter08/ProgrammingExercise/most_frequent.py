def main():
	user_str = input('Enter a string: ')

	frequent = most_frquent(user_str)
	print('Most Frequent Character Is:', frequent.upper())


def most_frquent(user_str):
	index = 0
	alphs = 'abcdefghijklmnopqrstuvwxyz'
	add_alphs = [0] * len(alphs)

	for ch in alphs:
		word_count = user_str.count(ch)
		add_alphs[index] += word_count
		index += 1

	most_frequent = max(add_alphs)
	freq_index = add_alphs.index(most_frequent)
	result = alphs[freq_index]

	return result

main()

