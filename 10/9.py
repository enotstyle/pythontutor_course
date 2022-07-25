n = int(input())
All = set()
One = set()
temp = set()
for i in range(n):
    k = int(input())
    for j in range(k):
        temp.add(input())
        if j == k-1 and i ==0:
            One |= temp
        if j == k-1:
            All |= temp
            One &= temp
            temp = set()
print(len(One), *sorted(One), sep='\n')
print(len(All), *sorted(All), sep='\n')