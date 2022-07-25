n = int(input())
a = [['.']*n for i in range(n)]
for i in range(len(a)):
    for j in range(len(a[i])):
        if (i == j) or (i == abs(j-(n-1))) or (i == n//2) or (j == n//2):
            a[i][j] = '*'
for i in a:
    print(' '.join(i))