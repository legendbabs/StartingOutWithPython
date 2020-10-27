def main():
	input_str = input('Enter a string and see its morse code: ')

	for char in input_str:
		result = test_str(char)
		print(result, end='')

def test_str(ch):
	if ch == ' ':
		return 'space'
	elif ch == ',':
		return '--..--'
	elif ch == '.':
		return '.-.-.-'
	elif ch == '?':
		return '..--..'
	elif ch == '0':
		return '-----'
	elif ch == '1':
		return '.----'
	elif ch == '2':
		return '..---'
	elif ch == '3':
		return '...--'
	elif ch == '4':
		return '....-'
	elif ch == '5':
		return '.....'
	elif ch == '6':
		return '-....'
	elif ch == '7':
		return '--...'
	elif ch == '8':
		return '---..'
	elif ch == '9':
		return '----.'
	elif ch.upper() == 'A':
		return '.-'
	elif ch.upper() == 'B':
		return '-...'
	elif ch.upper() == 'C':
		return '-.-.'
	elif ch.upper() == 'D':
		return '-..'
	elif ch.upper() == 'E':
		return '.'
	elif ch.upper() == 'F':
		return '..-.'
	elif ch.upper() == 'G':
		return '--.'
	elif ch.upper() == 'H':
		return '....'
	elif ch.upper() == 'I':
		return '..'
	elif ch.upper() == 'J':
		return '.---'
	elif ch.upper() == 'K':
		return '-.-'
	elif ch.upper() == 'L':
		return '.-..'
	elif ch.upper() == 'M':
		return '--.'
	elif ch.upper() == 'N':
		return '-.'
	elif ch.upper() == 'O':
		return '---'
	elif ch.upper() == 'P':
		return '.--.'
	elif ch.upper() == 'Q':
		return '--.-'
	elif ch.upper() == 'R':
		return '.-.'
	elif ch.upper() == 'S':
		return '...'
	elif ch.upper() == 'T':
		return '-'
	elif ch.upper() == 'U':
		return '..-'
	elif ch.upper() == 'V':
		return '...-'
	elif ch.upper() == 'W':
		return '.--'
	elif ch.upper() == 'X':
		return '-..-'
	elif ch.upper() == 'Y':
		return '-.-'
	elif ch.upper() == 'Z':
		return '--..'

main()

