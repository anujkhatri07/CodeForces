s = input()
 
letters = set()
 
for ch in s:
    if ch.isalpha():
        letters.add(ch)
 
print(len(letters))