t = int(input())
for i in range(t):
    n, k = map(int,input().split())
    gold = list(map(int, input().split()))
    people = 0
    money = 0
    for i in range(n):
        if gold[i] >= k:
            money += gold[i]
        if gold[i] == 0 and money > 0:
            people += 1
            money -= 1

    print(people)

