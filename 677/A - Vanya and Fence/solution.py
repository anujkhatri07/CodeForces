n, h = map(int, input().split())
a = list(map(int, input().split()))
 
width = 0
 
for x in a:
    if x > h:
        width += 2
    else:
        width += 1
 
print(width)