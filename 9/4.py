n = int(input())
a = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = abs(j-i)
for row in a:
    print(' '.join([str(i) for i in row]))