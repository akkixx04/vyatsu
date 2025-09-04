results = []
for _ in range(int(input())):
    n = int(input())
    enemy = input().strip()
    gregor = input().strip()

    max_quantity = 0
    enemy = list(enemy)

    for i in range(n):
        if gregor[i] == "1":
            if enemy[i] == "0":
                max_quantity += 1
            elif i > 0 and enemy[i - 1] == "1":
                max_quantity += 1
                enemy[i - 1] = "0"
            elif i < n - 1 and enemy[i + 1] == "1":
                max_quantity += 1
                enemy[i + 1] = "0"

    results.append(max_quantity)

for j in results:
    print(j)