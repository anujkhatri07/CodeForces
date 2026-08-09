n = int(input())
 
a = list(map(int, input().split()))
 
even = 0
odd = 0
 
for x in a:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
 
for i in range(n):
    if even == 1 and a[i] % 2 == 0:
        print(i + 1)
        break
    elif odd == 1 and a[i] % 2 != 0:
        print(i + 1)
        break