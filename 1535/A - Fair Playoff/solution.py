t = int(input())
 
for _ in range(t):
    s = list(map(int, input().split()))
 
    x = max(s[0], s[1])
    y = max(s[2], s[3])
 
    s.sort()
 
    if x == s[2] and y == s[3] or x == s[3] and y == s[2]:
        print("YES")
    else:
        print("NO")