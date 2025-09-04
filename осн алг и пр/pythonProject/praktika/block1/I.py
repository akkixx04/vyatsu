t = int(input())

numbers = [ ]

for i in range(t):
    n = int(input())
    numbers.append(n)

for n in numbers:
    a = n // 10
    b = n % 10
    print(a + b)