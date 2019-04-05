import math

n = int(input())
for i in range(1, n + 1):
    sqrt = int(math.sqrt(i))
    if(sqrt*sqrt == i):
     print(i)
