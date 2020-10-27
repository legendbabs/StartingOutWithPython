x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
result = 1

def multiplication(y, x, result):
    if y > 0:
        result *= x
        multiplication(y-1, x, result)
    if y == 1:
        print(result)
    
multiplication(y, x, result)