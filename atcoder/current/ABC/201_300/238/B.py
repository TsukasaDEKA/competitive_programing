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
        input = """4
90 180 45 195"""
        output = """120"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
1"""
        output = """359"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
215 137 320 339 341 41 44 18 241 149"""
        output = """170"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  agg = [0]
  for i in range(N):
    agg.append((A[i]+agg[-1])%360)
  agg.sort()
  agg.append(360)

  ans = 0
  for i in range(1, len(agg)):
    ans = max(ans, agg[i]-agg[i-1])
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()