t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    neg = a.count(-1)
 
    ans = 0
 
    while neg > n - neg or neg % 2 != 0:
        neg -= 1
        ans += 1
 
    print(ans)