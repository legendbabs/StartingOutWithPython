def main():
	video_file = open("video_times.txt", "w")
	
	print("How many videos do you want?", end="")
	
	num_videos = int(input(": "))
	
	for vid in range(1, num_videos+1):
		run_time = float(input("Video #" + str(vid) + ": "))
		video_file.write(str(run_time) + "\n")
		
	video_file.close()
	
	print("Run time written to video_times.txt.")
	
main()