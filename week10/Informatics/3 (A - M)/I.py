import math

x = int(input())
sum = 0

for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
        sum = sum + 1
        i = i + 1
if math.sqrt(x) == int(math.sqrt(x)):
    print(sum + 2 + (sum - 1))
else: print(sum + 2 + (sum))

