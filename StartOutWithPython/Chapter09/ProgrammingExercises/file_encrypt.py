import pickle

def main():
	codes = {
	"A": "%",
	"a": "9",
	"B": "@",
	"b": "#",
	"C": ":",
	"c": ";",
	"D": "'",
	"E": "(",
	"e": ")",
	"F": "{",
	"f": "}",
	"G": "<",
	"g": ">",
	"H": "=",
	"h": "-",
	"I": "+",
	"i": "*",
	"J": "/",
	"j": "^",
	"K": "%",
	"k": "$",
	"L": "|",
	"l": "!",
	"M": "?",
	"m": "_",
	"N": "8",
	"n": "7",
	"O": "6",
	"o": "5",
	"P": "4",
	"p": "3",
	"Q": "2",
	"q": "1",
	"R": "0",
	"r": ".",
	"S": ",",
	"s": "~",
	"T": "¡",
	"t": "!",
	"U": "[",
	"u": "]",
	"V": "¿",
	"v": "®",
	"W": "¤",
	"w": "β",
	"X": "€",
	"x": "Δ",
	"Y": "¥",
	"y": "£",
	"Z": "™",
	"z": "π"
	}
	print(len(codes))
	
	
	# writing to a file function
	write_file()
	
	# reading the contents of the file
	file_contents = read_file()
	
	# using a set function to read the file contents into dictionary
	set_file = set(file_contents)
	dict_content = open("dict.txt", "w")
#	print(set_file)
	for ch in set_file:
		if ch in codes:
			dict_content.write(codes[ch])
			
	dict_content.close()
	
	# display the contents of the code
	display_content()
			
#		print(ch)
#	file_split = file_contents.split()
#	set_content = set(file_contents)
#	print(file_split)

def write_file():
	outfile = open("text.txt", "w")
	user_str = input("Enter a string: ")
	outfile.write(user_str)
	outfile.close()
	
def read_file():
	infile = open("text.txt", "r")
	contents = infile.read()
	infile.close()
	
	return contents
	
def display_content():
	print("This is the coded version of your text.")
	infile = open("dict.txt", "r")
	content = infile.read()
	print(content)
	print()
	
	
#	print(contents)
	
#	output_file = open("file_encrypt.dat", "wb")
#	pickle.dump(codes, output_file)
#	output_file.close()
	
#	print("The codes has been written to file_encrypt.dat.")
	
main()
