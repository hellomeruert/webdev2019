n = int(input())
a = input().split()
found = False
for i in range(1, n):
    if (int(a[i])*int(a[i-1]) > 0):
        found = True
        break

if found:
    print('YES')
else:
    print('NO')

