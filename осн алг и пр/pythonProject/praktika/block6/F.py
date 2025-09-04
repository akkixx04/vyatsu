from math import log2

input()

for x in map(int,input().split()):
    b = 15

    for i in range(15):
        a = 1
        n = x + i
        while n & 1 != 1 and a <= 15:a += 1;n >>= 1
        b = min(15 - a + i ,b)

    print(b + 1,end = ' ')