R, C = map(int, input().split())
a = []

for i in range(R):
    row = input().replace(".", "D")
    if "SW" in row or "WS"in row :
        print("NO")
        exit(0)
    a.append(row)

for j in range(C):
    column = "".join(a[i][j] for i in range(R))
    if "SW" in column or "WS" in column:
        print("NO")
        exit(0)

print("YES")
for row in a:
    print(row)