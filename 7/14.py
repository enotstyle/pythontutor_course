# a = [int(i) for i in input().split()]
# for i in range(len(a)):
#     if a.count(a[i]) == 1:
#         print(a[i], end = ' ')

a = [int(i) for i in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end = ' ')