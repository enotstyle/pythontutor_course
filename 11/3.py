Dic = dict()
for i in range(int(input())):
    name, vote = input().split()
    Dic[name] = Dic.get(name, 0) + int(vote)
    # if name not in Dic:
    #     Dic[name] = int(vote)
    # else:
    #     Dic[name] += int(vote)
for key, val in sorted(Dic.items()):
    print(key, val)