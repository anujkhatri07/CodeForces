a = input().strip()
b = input().strip()
 
answer = ""
 
for i in range(len(a)):
    if a[i] == b[i]:
        answer += '0'
    else:
        answer += '1'
 
print(answer)