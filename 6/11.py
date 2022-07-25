n1 = int(input())
n2 = 0
x = -1
while n1 != 0:
    if n1 > n2:
        x += 1
    n2 = n1
    n1 = int(input())
print(x)