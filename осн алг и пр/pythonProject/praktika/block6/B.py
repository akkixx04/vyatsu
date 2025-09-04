t = int(input())
for i in range(t):
    l,r,x = map(int,input().split())
    a,b = map(int, input().split())
    res = 0
    if a == b:
        res = 0
    elif abs(a-b) >= x:
        res = 1
    elif r - max(a,b) >= x or min(a,b)-l >= x:
        res = 2
    elif ((r-a) >= x and (b-l)>=x) or ((a-l) >= x and (r-b) >= x):
        res = 3
    else: res =- 1
    print(res)