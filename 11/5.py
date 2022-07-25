Dic = dict()
for i in range(int(input())):
    mass = input().split()
    Dic[mass[0]] = mass
    del (Dic[mass[0]])[0]
for i in range(int(input())):
    mass = input().split()
    if mass[0] == 'read':
        if 'R' in Dic[mass[1]]:
            print('OK')
        else:
            print('Access denied')
    elif mass[0] == 'write':
        if 'W' in Dic[mass[1]]:
            print('OK')
        else:
            print('Access denied')
    elif mass[0] == 'execute':
        if 'X' in Dic[mass[1]]:
            print('OK')
        else:
            print('Access denied')