n = int(input())
a = list(map(int, input().split()))
 
count = 1
maximum = 1
 
for i in range(1, n):
    if a[i] > a[i - 1]:
        count += 1
    else:
        count = 1
 
    maximum = max(maximum, count)
 
print(maximum)