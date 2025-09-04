data = int(input())
for i in range(data):
    n, k = map(int, input().split())
    time = (n - 1) * k + 1
    print(time)