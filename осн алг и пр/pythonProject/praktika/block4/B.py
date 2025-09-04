for _ in range(int(input())):
    k, q = map(int, input().split())
    a = min(list(map(int, input().split())))
    def f(x):
        return min(int(x), a - 1)
    print(*list(map(f, input().split())))