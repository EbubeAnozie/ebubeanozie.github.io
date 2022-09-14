def primeChecker(number):
    for i in range(2, number):
        if number % i == 0:
            break
        elif i == number - 1:
            print(number)
