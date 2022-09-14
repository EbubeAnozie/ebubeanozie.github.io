"""
SPECIFICATION -->

Name:
ADD BINARY INTEGERS

What This Program Does:
It computes the sum of two binary numbers.

The Procedure:
It takes, as inputs, two arrays A and B of equal length(say n), with binary digits as elements.
The first operation is to reverse A and B. The idea is to start the arrays from the smallest power 
of base 2 for flexible sum operation that would allow room for surplus placeholder of carriers.
It adds the values in the 1st indices of the reversed A and reversed B; respectively assigns the mod2 and integer division
of the sum to the 1st and 2nd indices of a new array C. It iterates this opearions up to the last indices.
After the terminmation, the array C (of length n+1) holding the binary sum is reversed and returned as C.
"""
import time

start_time = time.time()

A = [1, 1, 1, 0, 1]
B = [1, 1, 1, 1, 1]
A.reverse()
B.reverse()
C = []
for i in range(0, len(A)):
    iSum = A[i] + B[i]
    rem = iSum % 2
    carry = iSum // 2
    C.append(rem)
    if i < len(A) - 1:
        A[i+1] = (carry) + A[i+1]
    else:
        C.append(carry)
        break
C.reverse()
print(C)

end_time = time.time()

elapsed_time = end_time - start_time  # The wall-clock time
print('Execution time:', elapsed_time, 'seconds')