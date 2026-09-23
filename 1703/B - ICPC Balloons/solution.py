t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input()
 
    solved = set()
    balloons = 0
 
    for problem in s:
        balloons += 1  # balloon for solving the problem
 
        if problem not in solved:
            balloons += 1  # extra balloon for first solve
            solved.add(problem)
 
    print(balloons)