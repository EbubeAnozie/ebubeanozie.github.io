import sys

a = int(input('Enter the dividend: '))
b = int(input('Enter the divisor: '))

Q = 0
R = a
while 0==0:
    if R < b:
        print('The quotient is ' + str(Q) + ' and the remainder is ' + str(R))
        sys.exit()
    elif R >= b:
        R -= b
        Q += 1
        continue