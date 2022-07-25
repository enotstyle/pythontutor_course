n = int(input())
A = set([str(i) for i in range(1, n+1)])
B = set(input().split())
while ("HELP" not in B):
    if input() == "NO":
        A -= B
    else:
        A = A & B
    B = set(input().split())
print(*sorted(A))