n = int(input())
p = 0
i1 = 1
i2 = 1
while n != 0:
    if n == p:
        i1+=1
    else:
        if i1 > i2:
            i2 = i1
        i1 = 1
    p = n
    n = int(input())
if i1>i2:
    print(i1)
else:
    print(i2)
