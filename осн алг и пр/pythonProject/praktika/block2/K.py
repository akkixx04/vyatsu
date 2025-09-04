t = int(input())
for i in range(t):
    a1, a2, b1, b2 = map(int, input().split())
    wins = 0
    if (a1 >= b1 and a2 > b2) or (a1 > b1 and a2 >= b2):
        wins += 2
    if (a1 >= b2 and a2 > b1) or (a1 > b2 and a2 >= b1):
        wins += 2
    else:
        wins = wins
    print(wins)