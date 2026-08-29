n = int(input())
a = list(map(int, input().split()))
 
max_height = max(a)
min_height = min(a)
 
# First maximum
max_index = a.index(max_height)
 
# Last minimum
min_index = n - 1 - a[::-1].index(min_height)
 
ans = max_index + (n - 1 - min_index)
 
# Maximum crosses the minimum
if max_index > min_index:
    ans -= 1
 
print(ans)