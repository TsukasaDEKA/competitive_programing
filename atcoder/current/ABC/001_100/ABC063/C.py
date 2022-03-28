import sys
from io import StringIO
import unittest

from numpy import sort

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
5
10
15"""
        output = """25"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
10
10
15"""
        output = """35"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
10
20
30"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = sorted([int(input()) for _ in range(N)])
  ans = sum(A)
  if ans%10:
    print(ans)
    return

  for i in range(N):
    if A[i]%10:
      print(ans-A[i])
      return
  else:
    print(0)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()