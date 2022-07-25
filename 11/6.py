Dic = dict()
for i in range(int(input())):
    mass = input().split()
    for i in mass:
        if i not in Dic:
            Dic[i] = 1
        else:
            Dic[i] += 1
A = []
B = []
for key, val in Dic.items():
    A.append((val, key))
A.sort(reverse=True)
for i in range(len(A)):
    B.append(A[i][1])
print('\n'.join(sorted(B)))