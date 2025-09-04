for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if sum(b) - sum(a) > n:
        print("NO")
    else:
        print("YES")