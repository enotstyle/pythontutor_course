from math import sqrt
def distance(x1, y1, x2, y2):
    return sqrt((abs(x1-x2))**2+(abs(y1-y2))**2)

print(distance(int(input()), int(input()), int(input()), int(input())))