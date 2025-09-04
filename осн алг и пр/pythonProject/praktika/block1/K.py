t = int(input())

numbers = [ ]

for i in range(t):
    n = int(input())
    numbers.append(n)

for n in numbers:
    print(3 if n == 3 else 2)