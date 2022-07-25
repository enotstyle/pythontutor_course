def power(a, n):
    x = 1
    for i in range(abs(n)):
        x*=a
    if n>=0:
        return x
    else:
        return 1/x
print(power(float(input()), int(input())))