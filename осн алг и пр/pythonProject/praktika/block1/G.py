data = int(input())
for i in range(data):
    a, b = map(int, input().split())
    c = b - a
    print((c - a) + (b - c))