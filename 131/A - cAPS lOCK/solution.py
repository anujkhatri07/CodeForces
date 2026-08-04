s = input()
 
if len(s) == 1:
    print(s.swapcase())
elif s.isupper() or s[1:].isupper():
    print(s.swapcase())
else:
    print(s)