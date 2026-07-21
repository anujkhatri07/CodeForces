oneb, money, banana = map(int, input().split())
 
cost = 0
 
for i in range(1, banana + 1):
    cost += i * oneb
 
if cost > money:
    print(cost - money)
else:
    print(0)