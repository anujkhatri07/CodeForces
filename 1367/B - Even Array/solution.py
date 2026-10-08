t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    even_wrong = 0
    odd_wrong = 0
 
    for i in range(n):
        if i % 2 == 0 and a[i] % 2 == 1:
            even_wrong += 1
        elif i % 2 == 1 and a[i] % 2 == 0:
            odd_wrong += 1
 
    if even_wrong != odd_wrong:
        print(-1)
    else:
        print(even_wrong)