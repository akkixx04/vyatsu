n = int(input())
t = list(map(float, input().split()))

lengths = []

type_sushi = t[0]
length = 1

for i in range(1, n):
    if t[i] == type_sushi:
        length += 1
    else:
        lengths.append(length)
        type_sushi = t[i]
        length = 1

lengths.append(length)

max_length = 0
for i in range(len(lengths) - 1):
    max_length = max(max_length, 2 * min(lengths[i], lengths[i + 1]))

print(max_length)