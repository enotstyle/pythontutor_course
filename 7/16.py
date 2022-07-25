a = []
x = 0
for i in range(8):
    a.extend([int(i) for i in input().split()])
for i in range(0, len(a), 2):
    for j in range(i+2, len(a), 2):
        if abs(a[i] - a[j]) == abs(a[i+1] - a[j+1]) or a[i] == a[j] or a[i+1] == a[j+1]:
            x += 1
if x == 0:
    print('NO')
else:
    print('YES')