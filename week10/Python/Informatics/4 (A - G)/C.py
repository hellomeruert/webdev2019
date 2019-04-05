n = int(input())
a = input().split()
count = 0
for i in range(n):
    if int(a[i]) > 0:
        count += 1
print(count)


