n = int(input())
a = input().split()
count = 0
for i in range(1, n - 1):
    if int(a[i]) > int(a[i-1]) and int(a[i]) > int(a[i+1]):
        count += 1
print(count)


