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
20 11 9 24"""
        output = """26 5 7 22"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  sum_ = A[0]
  for i in range(1, N):
    sum_^=A[i]
  ans = [sum_^x for x in A]
  print(*ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()