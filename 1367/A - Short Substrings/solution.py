t = int(input())
 
for _ in range(t):
    b = input().strip()
 
    if len(b) == 2:
        print(b)
    else:
        ans = b[0]
 
        for i in range(1, len(b), 2):
            ans += b[i]
 
        print(ans)