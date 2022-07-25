A = dict()
B = input().split()
for i in B:
    if i not in A:
        A[i] = 1
        print(0, end = ' ')
    else:
        print(A[i], end = ' ')
        A[i] += 1