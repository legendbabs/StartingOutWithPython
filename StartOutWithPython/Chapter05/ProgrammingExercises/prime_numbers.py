def main():
    number = int(input('Enter a number: '))

    prime = is_prime(number)

    if prime:
        print(number, 'is a prime number.')
    else:
        print(number, 'is not a prime number.')



def is_prime(number):

    counter = 0
    for num in range(2, number):
        if number % num == 0:
            counter += 1

    if counter == 0:
        return True
    else:
        return False


main()