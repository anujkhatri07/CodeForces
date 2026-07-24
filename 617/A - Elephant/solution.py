x = int(input())
 
 
moves = x // 5
 
 
if x % 5 != 0:
    moves += 1
 
print(moves)