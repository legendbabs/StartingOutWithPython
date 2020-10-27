import random

random.random()
random.randint(1, 5)
random.randrange(1, 10, 2)
random.shuffle([12, 34, 56, 60])
random.choice([1, 2, 3, 4, 5])
random.sample("abcdefghijklmnopqrstuvwxyz", 15)


num_str = random.sample("abcdefghijklmnopqrstuvwxyz1234567890", 15)
num_str = "".join([i for i in num_str])
print(num_str)
print()
for let in num_str:
	print(let, end="")



