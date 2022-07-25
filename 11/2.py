Dic = dict()
for i in range(int(input())):
    key, name = input().split()
    Dic[key] = name
temp = input()
for key, val in Dic.items():
    if temp == key:
        print(val)
    elif temp == val:
        print(key)
