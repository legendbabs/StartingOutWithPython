def main():
	name = input('What is your name? ')
	descr = input('Describe yourself in two sentences: ')

	html_result = f'''
		<!DOCTYPE html>
		<html>
			<head>
				<title></title>
			</head>
			<body>
				<center>
					<h1> {name} </h1>
				</center>

				<hr>
					{descr}
				</hr>

			</body>
		</html>
	'''

	print(html_result)

main()
