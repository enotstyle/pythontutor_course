N, M = [int(i) for i in input().split()]
A = set()
B = set()
for i in range(N):
    A.add(int(input()))
for i in range(M):
    B.add(int(input()))
print(len(A & B), ' '.join([str(i) for i in list(A & B)]), sep='\n')
print(len(A - B), ' '.join([str(i) for i in list(A - B)]), sep='\n')
print(len(B - A), ' '.join([str(i) for i in list(B - A)]), sep='\n')