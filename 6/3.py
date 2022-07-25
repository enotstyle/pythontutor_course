n = int(input())
kv = 1
i = 0
while kv*2 <= n:
    kv*=2
    i+=1
print(i, kv)
