# def main():
# 	biodata = open('biodata.txt', 'r')
# 	contents = biodata.read()
# 	biodata.close()

# 	print(contents)

# main()

myfile = open('friends.txt', 'a')
myfile.write('Kazim\n')
myfile.write('Mayowa\n')
myfile.write('Tomi\n')
myfile.close()
