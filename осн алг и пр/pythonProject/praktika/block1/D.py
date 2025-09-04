k = int(input())
for _ in range(k):
  n, d = map(int,input().split())
  a = sorted(list(map(int, input().split())))
  startI = 0
  maxLen = 0
  for i in range(1,n):
    if d < a[i] - a[i-1]:
      len = i - startI
      if len > maxLen:
        maxLen = len
      startI = i
  len = n - startI
  if len > maxLen:
    maxLen = len
  print(n - maxLen)