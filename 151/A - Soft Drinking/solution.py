n, k, l, c, d, p, nl, np = map(int, input().split())
 
drink = (k * l) // nl
lime = c * d
salt = p // np
 
total_toasts = min(drink, lime, salt)
 
answer = total_toasts // n
 
print(answer)