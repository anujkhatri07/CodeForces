t = int(input())
 
for _ in range(t):
 
    line = input().split()
    
    
    while len(line) == 0:
        line = input().split()
        
    
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    
    
    if a + b == c or a + c == b or b + c == a:
        print("YES")
    else:
        print("NO")