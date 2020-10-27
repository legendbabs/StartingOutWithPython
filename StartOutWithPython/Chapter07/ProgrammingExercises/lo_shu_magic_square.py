ROWS = 3
COLS = 3
def main():
	default_list = [
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]
	]
	
	# This is the magic square list
	magic_list = lo_shu_square(default_list)
	
	# row calculations
	row1 = magic_list[0][0] + magic_list[0][1] + magic_list[0][2]
	row2 = magic_list[1][0] + magic_list[1][1] + magic_list[1][2]
	row3 = magic_list[2][0] + magic_list[2][1] + magic_list[2][2]
	
	# column calculations
	col1 = magic_list[0][0] + magic_list[1][0] + magic_list[2][0]
	col2 = magic_list[0][1] + magic_list[1][1] + magic_list[2][1]
	col3 = magic_list[0][2] + magic_list[1][2] + magic_list[2][2]
	
	# calculations for diagonals
	dia1 = magic_list[0][0] + magic_list[1][1] + magic_list[2][2]
	dia2 = magic_list[0][2] + magic_list[1][1] + magic_list[2][0]
	
	if row1 == row2 == row3 == col1 == col2 == col3 == dia1 == dia2:
		print("This is a Lo Shu Magic Square.")
		
	else:
		print("Not A Lo Shu Magic Square.")
	
	
def lo_shu_square(sqr_list):
	for r in range(ROWS):
		for c in range(COLS):
			sqr_list[r][c] = int(input("Enter the values for row" + str(r+1) + "," + "col" + str(c+1) + ": "))
			
	return sqr_list
			
#	print()
#	print(sqr_list)
#	print()
	
	
main()