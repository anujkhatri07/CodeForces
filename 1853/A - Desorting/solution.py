t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    if a != sorted(a):
        print(0)
    else:
        ans = min(a[i + 1] - a[i] for i in range(n - 1))
        print(ans // 2 + 1)