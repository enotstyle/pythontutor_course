a = [int(i) for i in input().split()]
x = 0
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        print(a[i], end = ' ')