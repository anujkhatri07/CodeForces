n = int(input())
 
teams = []
 
for _ in range(n):
    h, a = map(int, input().split())
    teams.append((h, a))
 
ans = 0
 
for i in range(n):
    for j in range(n):
        if i != j:
            # Team i is host, team j is guest
            if teams[i][0] == teams[j][1]:
                ans += 1
 
print(ans)