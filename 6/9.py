mx = 0
mxi = 0
i = 0
n = int(input())
while n!=0:
    if n > mx:
        mx = n
        mxi = i
    n = int(input())
    i+=1
print(mxi)