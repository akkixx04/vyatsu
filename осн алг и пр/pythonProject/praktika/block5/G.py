n = int(input())
p = list(map(int, input().strip().split()))
for i in range(1, n + 1):
    a = [0 for i in range(n + 1)]
    a[i] = 1
    j = p[i - 1]
    while True:
        if a[j] == 0:
            a[j] = 1
            j = p[j - 1]
        else:
            print(j, end = " ")
            break
print( )