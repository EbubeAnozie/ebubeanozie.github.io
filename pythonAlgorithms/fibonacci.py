from time import sleep


def fibonacci():
    a, b = 1, 1
    while True:
        sleep(0.3)
        print(a)
        a, b = b, a + b


fibonacci()
