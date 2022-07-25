def capitalize(x):
    return (chr(ord(x) - 32))

a = input().split()
for i in a:
    b = list(i)
    b[0] = capitalize(b[0])
    print(''.join(b), end=' ')
