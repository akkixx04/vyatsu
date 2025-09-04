n = int(input())
p = [int(input()) for _ in range(n)]

min_groups = 0

for i in range(1, n + 1):
    count = 0
    employee = i
    while employee != -1:
        employee = p[employee - 1]
        count += 1
    min_groups  = max(min_groups, count)

print(min_groups)