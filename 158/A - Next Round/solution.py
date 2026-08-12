n, k = map(int, input().split())
a = list(map(int, input().split()))
 
count = 0
 
for score in a:
    if score >= a[k - 1] and score > 0:
        count += 1
 
print(count)