Dic = dict()
B = dict()
n = int(input())
for i in range(n):
    A = input().split(' - ')
    A.extend(A[1].split(', '))
    del A[1]
    Dic[A[0]] = (A[1:])
    A.clear()
for val in Dic.values():
    A.extend(val)
A = set(A)
for i in sorted(A):
    B[i] = []
for i in A:
    for key, val in Dic.items():
        if i in val:
            B[i].append(key)
print(len(B))
for key, val in B.items():
    print(key, '-', ', '.join(val))