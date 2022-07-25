n = input()
k = str()
for i in range(len(n)):
    if i % 3 != 0:
        k += n[i]
print(k)