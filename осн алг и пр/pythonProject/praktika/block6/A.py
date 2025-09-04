n, t = map(int, input().split())
s = input().strip()

a = list(s)

for j in range(t):
    i = 0
    while i < n - 1:
        if a[i] == 'B' and a[i + 1] == 'G':
            a[i], a[i + 1] = a[i + 1], a[i]
            i += 1
        i += 1

res = ''.join(a)
print(res)