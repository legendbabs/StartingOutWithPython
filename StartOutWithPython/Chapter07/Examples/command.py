started = False
command = ""

while command == "":
	print("Enter (START) to start the Car OR (STOP) to stop the Car.")
	command = input(": ").lower()
	if command == "start":
		if started:
			print("Car already started !!!")
		else:
			started = True
			print("Car started...")
			
	elif command == "stop":
		if not started:
			print("Car already stopped...")
		else:
			started = False
			print("Car stopped...")
			
	command = ""