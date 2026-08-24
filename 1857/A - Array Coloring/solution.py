t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    odd = sum(x % 2 for x in a)
 
    if odd % 2 == 0:
        print("YES")
    else:
        print("NO")