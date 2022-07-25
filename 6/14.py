n = int(input())
f0 = 0
f1 = 1
for i in range(2, n+2):
    f0, f1 = f1, f0+f1
print(f0)


n = int(input())
f0 = 0
f1 = 1
i = 0
while i != n:
    f0, f1 = f1, f0+f1
    i+=1
print(f0)