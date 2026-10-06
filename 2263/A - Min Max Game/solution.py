t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    ones = a.count(1)
    zeros = n - ones
 
    if ones >= zeros:
        print("Bessie")
    else:
        print("Elsie")