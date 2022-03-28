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
        input = """7
3 1 4 1 5 9 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10
0 1 2 3 4 5 6 7 8 9"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
99999"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  agg = defaultdict(int)
  ans = 0
  for i in range(N):
    for j in range(-1, 2):
      agg[A[i]+j]+=1
      ans = max(ans, agg[A[i]+j])

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()