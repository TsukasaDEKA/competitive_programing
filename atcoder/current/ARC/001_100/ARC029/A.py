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
4
6
7
10"""
        output = """14"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1
2
4"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
29"""
        output = """29"""
        self.assertIO(input, output)

def resolve():
  from itertools import permutations

  inf = 10**18+1
  N = int(input())
  A = [int(input()) for _ in range(N)]
  sum_ = sum(A)
  ans = inf
  for i in range(N+1):
    for tar in permutations(A, i):
      ans = min(ans, max(sum_-sum(tar), sum(tar)))
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()