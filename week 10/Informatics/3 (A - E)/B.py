import math

i = 2
n = int(input())
while i <= n:
    if n % i == 0:
        print(i)
        break
    i+=1

