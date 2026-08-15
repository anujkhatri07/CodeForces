r = 0
c = 0
 
for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        if row[j] == 1:
            r = i
            c = j
 
print(abs(r - 2) + abs(c - 2))