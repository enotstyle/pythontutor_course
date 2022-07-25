# a = [int(i) for i in input().split()]
# max_el = a.index(max(a))
# min_el = a.index(min(a))
# a[max_el], a[min_el] = a[min_el], a[max_el]
# print(' '.join([str(i) for i in a]))

a = [int(i) for i in input().split()]
max_in = 0
min_in = 0
for i in range(1, len(a)):
    if a[i] > a[max_in]:
        max_in = i
    if a[i] < a[min_in]:
        min_in = i
a[max_in], a[min_in] = a[min_in], a[max_in]
print(' '.join([str(i) for i in a]))