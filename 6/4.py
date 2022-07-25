x = int(input())
y = int(input())
i = 1
while x < y:
    x += (10*(x/100))
    i += 1
print(i)