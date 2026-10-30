t = int(input())
 
for _ in range(t):
    a, b, c, n = map(int, input().split())
 
    m = max(a, b, c)
    need = (m - a) + (m - b) + (m - c)
 
    if n >= need and (n - need) % 3 == 0:
        print("YES")
    else:
        print("NO")