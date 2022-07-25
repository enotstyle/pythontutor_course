A = [int(i) for i in input().split()]
B = set()
for i in A:
    if i not in B:
        print('NO')
        B.add(i)
    else:
        print('YES')