def main():
	num_videos = int(input('How many videos are in the project? '))
	video_file = open('video_times.txt', 'w')

	print('Enter the running times for each video.')

	for count in range(1, num_videos+1):
		run_time = float(input('Video #' + str(count) + ': '))
		video_file.write(str(run_time) + '\n')

	video_file.close()

	print('The times has been saved to video_times.txt.')

main()