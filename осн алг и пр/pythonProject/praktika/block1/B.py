t = int(input())

sin = [ ]

for i in range(t):
    n = int(input())
    sin.append(n)

for n in sin:
    choc = (4 * n + (2 * n) * n)//2+2
    print(choc)