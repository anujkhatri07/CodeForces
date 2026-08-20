n, k = map(int, input().split())
 
available = 240 - k
time = 0
solved = 0
 
for i in range(1, n + 1):
    time += 5 * i
 
    if time <= available:
        solved += 1
    else:
        break
 
print(solved)