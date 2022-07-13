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
        input = """4 2
abi
aef
bc
acg"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2
a
b"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 2
abpqxyz
az
pq
bc
cy"""
        output = """7"""
        self.assertIO(input, output)

def resolve():
  from collections import Counter, defaultdict
  inf = 10**18+1
  N, K = map(int, input().split(" "))
  S = []
  for i in range(N):
    S.append(list(input()))

  ans = 0
  for bit in range(1, 1<<N):
    agg = defaultdict(int)
    for i in range(N):
      if (1<<i)&bit:
        for s in S[i]:
          agg[s]+=1

    count = 0
    for val in agg.values():
      if val==K:
        count += 1
    ans = max(ans, count)



  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()