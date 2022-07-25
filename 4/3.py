a = int(input())
b = int(input())
for i in range((a-1)+(a%2), (b-1)-(b%2), -2):
    print(i, sep = ' ', end = ' ')