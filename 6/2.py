x = int(input())
i = x
nat = 0
while i != 1:
    if x % i == 0:
        nat = i
    i -= 1
print(nat)