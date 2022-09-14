"""
SPECIFICATION ->

Name:
Insertion sort algorithm

What this program will do:
This program will sort a given sesquence of finite numbers into
a monotone nondecreasing sequence.

How it will achieve this:
The operation will focus on position, hence will use array as the data structure
since arrray assigns positions(indices) to some satelite data.
The sort will start from left to right. It will activate the current value in key index
(starting from the first), and compares it with the value in the lower (adjecent) index.
"""

import time

start_time = time.time()    # To measure the wall-clock time
st = time.process_time()    # To measure CPU execution time


def INSERTION_SORT(A):
    for j in range(len(A)):
        try:
            key = (A[j])
            i = j-1
            while -1 < i and key < (A[i]):
                A[i+1] = (A[i])
                i = i-1
            A[i+1] = key
        except ValueError:
            None
    print(A)


INSERTION_SORT([2, 3, 4.0, 3, 5883843, 48483, 22, 42424])

end_time = time.time()
et = time.process_time()

elapsed_time = end_time - start_time
res = et - st

print('CPU Execution time:', res, 'seconds')
print('Execution time:', elapsed_time, 'seconds')
