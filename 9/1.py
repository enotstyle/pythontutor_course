n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
mx = a[0][0]
i_m = 0
j_m = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] > mx:
            mx = a[i][j]
            i_m = i
            j_m = j
print(i_m, j_m)