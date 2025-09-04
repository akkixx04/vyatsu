for _ in range(int(input())):
    a, b = map(int, input().split())
    res = min((a + b) // 4, a, b)
    print(res)