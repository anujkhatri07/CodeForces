n = int(input())
word = input()
 
count_A = 0
 
for i in range(n):
    if word[i] == 'A':
        count_A += 1
 
count_D = n - count_A
 
if count_A > count_D:
    print("Anton")
elif count_A == count_D:
    print("Friendship")
else:
    print("Danik")