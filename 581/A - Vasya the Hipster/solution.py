a, b = map(int, input().split())
 
different = min(a, b)
same = abs(a - b) // 2
 
print(different, same)