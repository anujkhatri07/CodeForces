t = int(input())
 
for _ in range(t):
    x1, x2, x3 = map(int, input().split())
 
    a = sorted([x1, x2, x3])
 
    print(a[2] - a[0])