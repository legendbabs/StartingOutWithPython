def main():
	filename = input("Enter a filename: ")
	
	try:
		infile = open(filename, "r")
		contents = infile.read()
		print("The contents of", "(", filename, ") are...")
		print("-------------------------------------")
		print()
		print(contents)
		
		infile.close()
		
	except IOError:
		print("The file", filename, "is not found.")
	
main()