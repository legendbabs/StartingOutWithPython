# File read using while loop

"""def main():
	total = 0.0
	count = 0
	
	video_file = open("video_times.txt", "r")
	line = video_file.readline()
	
	while line != "":
		amount = float(line)
		count += 1
		print("Video #", count, ": ", amount, sep="")
		
		total += amount
		line = video_file.readline()
	
	video_file.close()
	
	print("Total runtime is:", format(total, ".1f"), "seconds.")
	
main()
"""

# File read using for loop

def main():
	total = 0.0
	count = 0
	
	video_file = open("video_times.txt", "r")
	for line in video_file:
		amount = float(line)
		count += 1
		
		print("Video #", count, ": ", amount, sep="")
		
		total += amount
		
	video_file.close()
	
	print("Total runtime is:", format(total, ".1f"), "seconds.")
	
main()
		
		
		