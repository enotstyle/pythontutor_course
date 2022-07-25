n = int(input())
x = n-1
a = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if j == x:
            a[i][j] = 1
        elif j > x:
            a[i][j] = 2
        else:
            a[i][j] = 0
    x -= 1
for row in a:
    print(' '.join([str(i) for i in row]))