t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input()
 
    first = s.find('B')
    last = s.rfind('B')
 
    print(last - first + 1)