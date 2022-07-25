now = int(input())
maxi = 0
kol = 0
while now != 0:
    if now == maxi:
        kol += 1
    if now > maxi:
        maxi = now
        kol = 1
    now = int(input())
print(kol)