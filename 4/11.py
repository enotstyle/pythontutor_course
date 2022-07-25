n = int(input())
s = 0
c = 0
for i in range(1, n):
    c += i
    s += int(input())
print((c+n)-s)