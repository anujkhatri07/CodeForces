t = int(input())
 
target = sorted("Timur")
 
for _ in range(t):
    n = int(input())
    s = input()
 
    if n == 5 and sorted(s) == target:
        print("YES")
    else:
        print("NO")