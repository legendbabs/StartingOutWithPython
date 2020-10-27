def main():
    number = int(input('Enter a number: '))

    prime = is_prime(number)

    if prime:
        print(number, 'is a prime number.')
    else:
        print(number, 'is not a prime number.')



def is_prime():
    for test_num in range(1, 101):

        counter = 0
        for num in range(2, test_num):
            if test_num % num == 0:
                counter += 1

        


main()