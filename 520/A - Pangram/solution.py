n = int(input())
s = input().lower()
 
alphabet = "abcdefghijklmnopqrstuvwxyz"
 
for ch in alphabet:
    if ch not in s:
        print("NO")
        break
else:
    print("YES")