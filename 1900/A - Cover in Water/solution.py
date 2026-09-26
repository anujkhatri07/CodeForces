t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input().strip()
 
    # If there are 3 consecutive empty cells,
    # they can be filled using only 2 type-1 operations.
    if "..." in s:
        print(2)
    else:
        print(s.count('.'))