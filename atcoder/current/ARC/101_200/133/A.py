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
        input = """5
2 4 4 1 2"""
        output = """2 1 2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 1 1"""
        output = """"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
1 1 2 3 3"""
        output = """1 1 2"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5
2 1 1 3 3"""
        output = """1 1 3 3"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  m = max(A)
  ans = [x for x in A if x != m]
  x = -1
  for i in range(1, N):
    if A[i-1] > A[i]:
      x = A[i-1]
      break
  else:
    x = max(A)

  ans = [m for m in A if m != x]

  print(*ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()