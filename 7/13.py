a = [int(i) for i in input().split()]
x = 0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j]:
            x+=1
        if i == j:
            x-=1
print(int(x/2))