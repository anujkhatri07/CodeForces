t = int(input())
 
for _ in range(t):
    a, b = input().split()
 
    x = a[0]
    y = b[0]
 
    a = y + a[1:]
    b = x + b[1:]
 
    print(a, b)