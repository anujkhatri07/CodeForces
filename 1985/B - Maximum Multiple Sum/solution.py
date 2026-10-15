t = int(input())
 
for _ in range(t):
    n = int(input())
    ans = 2
    max_sum = 0
 
    for x in range(2, n + 1):
        total = sum(range(x, n + 1, x))
 
        if total > max_sum:
            max_sum = total
            ans = x
 
    print(ans)