n, m = [int(i) for i in input().split()]
a = [['*']*m for i in range(n)]
for i in range(len(a)):
    for j in range(len(a[i])):
        if (i%2 != 1):
            if (j%2 != 1):
                a[i][j] = '.'
        else:
            if (j%2 == 1):
                a[i][j] = '.'
for i in a:
    print(' '.join(i))