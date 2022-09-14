"""THIS PYTHON PROGRAM USES A FUNCTION THAT CHECKS
   THE PRIMALITY OF A NUMBER (< 10^8, if prime) FROM THE USER"""


# Define a function with primality algorithm:
def primeChecker(number):
    for i in range(2, number):
        if number % i == 0:
            print(str(number) + ' is COMPOSITE!\n' + str(i) + ' is its first prime factor.')
            break
        else:
            None
            if i == number - 1:
                print(str(number) + ' is PRIME!')


while True:
    number = int(input('Enter number\n>>> '))
    primeChecker(number)
    continue