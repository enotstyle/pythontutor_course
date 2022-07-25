# a = [int(i) for i in input().split()]
# print(' '.join([str(i) for i in a[::2]]))

a = input().split()
for i in range(0, len(a), 2):
    print(a[i], end=' ')

