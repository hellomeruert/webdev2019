import math

def f(a, n):
    return pow(a,n)

a, n = map(float, input().split())
x = float(f(a, n))
print(x)
