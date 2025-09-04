import random
A = [random.randint(-99, 67) for _ in range(30)]
B = [x for x in A if x % 2 == 0]
print(A)
print(B)