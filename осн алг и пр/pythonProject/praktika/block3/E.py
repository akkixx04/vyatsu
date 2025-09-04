t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    bananas = [a, b, c]
    operations = 0
    P = 1
    while operations < 5:
            min_number = min(bananas)
            bananas.remove(min_number)
            min_number += 1
            bananas.append(min_number)
            operations += 1
    for i in bananas:
        P *= i
    print(P)