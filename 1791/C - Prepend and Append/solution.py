t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input()
 
    left = 0
    right = n - 1
 
    while left < right and s[left] != s[right]:
        left += 1
        right -= 1
 
    print(right - left + 1)