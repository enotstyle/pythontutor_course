def swap_columns(a, i, j):
    for x in range(len(a)):
        a[x][i], a[x][j] = a[x][j], a[x][i]


n, m = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]
swap_columns(a, i, j)
# for i in range(len(a)):
#     print(' '.join(str(i) for i in a[i]))
print('\n'.join([' '.join([str(i) for i in a[i]]) for a[i] in a]))