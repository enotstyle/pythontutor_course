f = 1
s = 0
n = int(input())
for i in range(1, n+1):
    f *= i
    s += f
print(s)