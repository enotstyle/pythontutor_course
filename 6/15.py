A = int(input())
f0 = 0
f1 = 1
i = 1
while f1 != A:
    f0, f1 = f1, f0+f1
    i+=1
    if f1 > A:
        print(-1)
        break
else:
    print(i)