Dic = dict()
for i in range(int(input())):
    A = input().split()
    Dic[A[0]] = A[1:]
for i in range(int(input())):
    _ = input()
    for key, val in Dic.items():
        if _ in val:
            print(key)