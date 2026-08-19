x = list(map(int, input().split()))
 
x.sort()
 
S = x[3]
 
a = S - x[2]
b = S - x[1]
c = S - x[0]
 
print(a, b, c)