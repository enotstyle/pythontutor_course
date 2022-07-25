a = [int(i) for i in input().split()]
k, c = [int(i) for i in input().split()]
a.append(c)
print(a)
for i in range(-1, k-len(a), -1):
    a[i], a[i-1] = a[i-1], a[i]
print(a)