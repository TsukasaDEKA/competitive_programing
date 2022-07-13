import sys
ans = 0
for s in list(input()):
  ans += 1 if s == "+" else -1

print(ans)
