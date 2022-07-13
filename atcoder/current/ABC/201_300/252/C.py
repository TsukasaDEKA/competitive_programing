import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """3
1937458062
8124690357
2385760149"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
0123456789
0123456789
0123456789
0123456789
0123456789"""
        output = """40"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  from collections import defaultdict

  inf = 10**18+1
  N = int(input())
  S = [[int(x) for x in list(input())] for _ in range(N)]
  agg = defaultdict(list)
  for s in S:
    for i in range(10):
      agg[s[i]].append(i)

  ans = inf
  for i in range(10):
    agg[i].sort()
    que = deque(agg[i])
    temp = inf
    used = set()
    while que:
      p = que.popleft()
      if p not in used:
        temp = p
        used.add(p)
      else:
        que.append(p+10)
    ans = min(ans, temp)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()