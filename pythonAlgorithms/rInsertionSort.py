while True:
    B = input("Enter the numbers to be sorted seperated by comma:\n")
    A = B.split(',')
    for j in range(1,len(A)):
        try:
            key = int(A[j])
            i = j-1
            while i > -1 and int(A[i]) < key:
                A[i+1] = int(A[i])
                i = i-1
            A[i+1] = key
        except ValueError:
            None
    print(A)