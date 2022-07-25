n = int(input())
A = dict()
for i in range(n):
    B = input().split()
    for j in B:
        A[j] = A.get(j, 0) + 1

max_count = max(A.values())
most_frequent = [k for k, v in A.items() if v == max_count]
print(min(most_frequent))