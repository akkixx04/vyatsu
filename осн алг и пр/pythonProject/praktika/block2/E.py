for i in range(int(input())):
    p1, p2, p3 = map(int, input().split())
    S = p1 + p2 + p3
    if S % 2 == 0:
        if p1 + p2 <= p3:
            print(p1 + p2)
        else:
            print(S // 2)
    else:
        print(-1)