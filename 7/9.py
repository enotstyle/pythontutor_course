a = [int(i) for i in input().split()]
c = 0
for i in range(0, len(a) - len(a) % 2, 2):
    a[i], a[i + 1] = a[i + 1], a[i]
print(*a)
print(' '.join([str(i) for i in a]))