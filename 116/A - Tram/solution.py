n = int(input())
 
inside = 0
capacity = 0
 
for _ in range(n):
    a, b = map(int, input().split())
 
    inside -= a
 
    inside += b
 
    capacity = max(capacity, inside)
 
print(capacity)