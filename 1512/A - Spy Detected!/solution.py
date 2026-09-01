t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    if a[0] == a[1]:
        common = a[0]
        for i in range(2, n):
            if a[i] != common:
                print(i + 1)
                break
    else:
        if a[0] == a[2]:
            print(2)
        else:
            print(1)