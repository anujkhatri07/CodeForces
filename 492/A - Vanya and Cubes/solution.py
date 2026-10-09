n = int(input())
 
height = 0
cubes = 0
level = 1
 
while True:
    cubes += level * (level + 1) // 2
 
    if cubes > n:
        break
 
    height += 1
    level += 1
 
print(height)