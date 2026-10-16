t = int(input())
 
for _ in range(t):
    n, m = map(int, input().split())
 
    available = set()
 
    for i in range(n):
        word = input()
        available.add(word[0].upper())
 
    a = []
    for i in range(m):
        a.append(input())
 
    done = [False] * m
    count = 0
 
    while count < m:
        progress = False
 
        for i in range(m):
            if done[i]:
                continue
 
            possible = True
 
            for ch in a[i]:
                if ch not in available:
                    possible = False
                    break
 
            if possible:
                available.add(a[i][0])
                done[i] = True
                count += 1
                progress = True
 
        if not progress:
            break
 
    if count == m:
        print("YES")
    else:
        print("NO")