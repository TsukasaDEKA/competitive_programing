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
        input = """6
2 1 2 1 1 10"""
        output = """4
2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7
3 1 4 1 5 9 2"""
        output = """5.250000000
4"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  A = sorted([(x, i) for i, x in enumerate([int(x) for x in input().split(" ")])])

  vals = []
  droped = set()
  for i in range(N):
    x, j = A[i]
    if j+1 in droped or j-1 in droped:
      vals.append(x)
    else:
      droped.add(j)

  avg = sum(vals)/len(vals)
  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()