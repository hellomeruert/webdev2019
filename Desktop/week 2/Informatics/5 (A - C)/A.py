import  math

def f(a,b,c,d):
    return min(min(a,b), min(c,d))

a, b, c, d = map(str, input().split())
x = f(a,b,c,d)
print(x)

