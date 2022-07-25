n = int(input())
A = set([str(i) for i in range(1, n+1)])
B = set(input().split())
pos = A
while ("HELP" not in B):
    if len(pos & B) > len(pos) / 2:
        print('YES')
        pos &= B
    else:
        print('NO')
        pos &= A - B
    B = set(input().split())
print(*sorted(pos))