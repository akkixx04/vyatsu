for _ in range(int(input())):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ops = 0
    print(2 * (n - max(p)) - k + 1)
    
    # while len(p) > 1:
    #     min_n = min(p)
    #     max_n = max(p)
    #     if min_n == 1:
    #         p.remove(max_n)
    #         p.remove(min_n)
    #         p.append(min_n + max_n)
    #         ops += 1
    #     else:
    #         p.remove(min_n)
    #         p.append(1)
    #         p.append(min_n - 1)
    #         ops += 1
    # print(ops)