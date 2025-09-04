k = int(input())
for _ in range(k):
  n = int(input())
  a = list(map(int, input().split()))
  if n < 3:
    print("YES\n")
    continue
  flagNo = False
  flagMin = False
  for i in range(1, n):
    if a[i]<a[i-1]:
      flagMin = True
    if flagMin and a[i]>a[i-1]:
      flagNo = True
      break
  if flagNo:
    print("NO\n")
  else:
    print("YES\n")