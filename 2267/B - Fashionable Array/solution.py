from collections import Counter
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    freq = Counter(a)
    ans = []
 
    mx = max(freq.values())
 
    for k in range(1, mx + 1):
        for x in sorted(freq.keys(), reverse=True):
            if freq[x] >= k:
                ans.append(x)
 
    print(*ans)