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
1 10 15
1 11 12
1 14 16"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 20 22
1 22 24
2 0 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
2 0 24
1 0 10
3 0 1
1 12 23
3 22 24"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]

  A = sorted([[D*24+S, D*24+T] for D, S, T in A])
  for i in range(1, N):
    if A[i-1][1] > A[i][0]:
      print("Yes")
      return
  print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()