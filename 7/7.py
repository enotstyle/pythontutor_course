a = [int(i) for i in input().split()]
n = int(input())
x = 0
for i in range(len(a)):
    if a[i]>=n:
        x+=1
print(x+1)