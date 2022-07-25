a = [int(i) for i in input().split()]
# print(max(a), a.index(max(a)))
max_in = 0
for i in range(1, len(a)):
    if a[i] > a[max_in]:
        max_in = i
print(a[max_in], max_in)