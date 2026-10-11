t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    m = min(a)
    ans = sum(x - m for x in a)
 
    print(ans)