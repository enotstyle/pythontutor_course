def rec():
    x = int(input())
    if x == 0:
        print(x)
        return
    rec()
    print(x)

rec()