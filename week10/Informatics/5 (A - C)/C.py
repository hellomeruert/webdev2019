import math

def Xor(x, y):
    if x == 0 and y == 1:
        return 1
    if x == 1 and y == 0:
        return 1
    else:
        return 0

x, y = map(int, input().split())
res = Xor(x, y)
print(res)

