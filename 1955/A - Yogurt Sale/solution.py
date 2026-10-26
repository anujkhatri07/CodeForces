t = int(input())
 
for _ in range(t):
    n, a, b = map(int, input().split())
 
    cost = (n // 2) * min(b, 2 * a) + (n % 2) * a
 
    print(cost)