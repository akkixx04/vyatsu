q = int(input())
for _ in range(q):
    s = input()
    t = input()

    sec = 0
    s1 = len(s)
    t1 = len(t)

    for i in range(1, min(s1, t1) + 1):
        if s[:i] == t[:i]:
            sec = i

    print(s1 + t1 - max(sec, 1) + 1)