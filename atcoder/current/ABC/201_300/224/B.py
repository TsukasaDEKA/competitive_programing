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
        input = """3 3
2 1 4
3 1 3
6 4 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 4
4 3 2 1
5 6 7 8"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  H, W = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(H)]

  for i_1 in range(H-1):
    for i_2 in range(i_1+1, H):
      for j_1 in range(W-1):
        for j_2 in range(j_1+1, W):
          if A[i_1][j_1]+A[i_2][j_2] > A[i_2][j_1]+A[i_1][j_2]:
            print("No")
            return



  print("Yes")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()