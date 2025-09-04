data = int(input())
for i in range(data):
    n = int(input())
    points = list(map(int,input().split()))
    if n == 2 and points[1] - points[0] > 1:
        print("YES")
    else:
        print("NO")