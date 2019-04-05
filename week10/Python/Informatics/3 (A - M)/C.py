import math

a = int(input())
b = int(input())

sqrt_a = math.ceil(math.sqrt(a + 0.0))
sqrt_b = (math.sqrt(float(b)))
for i   in range(sqrt_a - 1, int(sqrt_b)):
    i = i + 1
    print(i*i, ' ')





