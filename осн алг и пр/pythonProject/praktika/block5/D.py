n, d = map(int, input(). split())
s = input().strip()

q = [0]
j = [-1] * n
j[0] = 0

while q:
    c = q.pop(0)

    for i in range(1, d + 1):
        next = c + i
        if next < n and s[next] == "1" and j[next] == -1:
            j[next] = j[c] + 1
            q.append(next)
            if next == n - 1:
                print(j[next])
                exit()

print(-1)