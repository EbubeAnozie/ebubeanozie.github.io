"""
SPECIFICATION:

What This Program Will Do:
It will sort n numbers stored in an array, A.

Procedures This Program Will Take:
STAGE 1: It will first find the smallest element of
A[0:n] using the following algorithm, viz;
>take the first element as the smallest;
>compare with the element in next index, and assign to smallest accordingly;
>continue in this mannner up to the last index of the array.
STAGE 2: It will exchange the smallest element with the element in A[0].
STAGE 3: Then repeat STAGES 1 and 2 for A[1:n]. Continue in this manner
for the first n-1 elements of A.

"""
A = [5, 4, 3, 2, 1]
for j in range(0, len(A)-1):
    smallest = A[j]
    index = j      # Remembers the current index of the smallest.
    for i in range(j+1, len(A)):
        if A[i] < smallest:
            smallest = A[i]
            index = i
        else:
            smallest = A[index]
    A[index] = A[j]
    A[j] = smallest
print(A)  