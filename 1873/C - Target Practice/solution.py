t = int(input())
 
for _ in range(t):
    grid = []
 
    for i in range(10):
        grid.append(input())
 
    score = 0
 
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'X':
                ring = min(i, j, 9 - i, 9 - j)
                score += ring + 1
 
    print(score)