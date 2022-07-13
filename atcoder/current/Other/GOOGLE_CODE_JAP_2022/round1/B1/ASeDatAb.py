import sys
from random import randrange
table = [set() for _ in range(9)]
popcnt = lambda x: bin(x).count("1")

for i in range(1<<8):
  s = f'{i:08b}'
  c = popcnt(i)
  for r in range(8):
    s_ = s[r:] + s[:r]
    if s_ in table[c]:
      break
  else:
    table[c].add(s)

for i in range(1, 9):
  table[i] = list(table[i])

result = []
T = int(input())
for t in range(T):
  print("00000001")
  V = int(input())

  for i in range(299):
    print(table[V][randrange(0, len(table[V]))])
    V = int(input())
    if V == 0 or V == -1:
      print(i, file=sys.stderr)
      result.append(i)
      break

print(sorted(result), file=sys.stderr)
