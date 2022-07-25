n, k = [int(i) for i in input().split()]
a = ['I']*n
for i in range(k):
    I, R = [int(i) for i in input().split()]
    for j in range(I-1, R):
        a[j]='.'
print(''.join(a))