import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
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
0 0
1 2
2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
-691 273"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
-31 -35
8 -36
22 64
5 73
-14 8
18 -58
-41 -85
1 -88
-21 -85
-11 82"""
        output = """11"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  N = int(input())
  if N  == 1:
    print(0)
    return

  X_Y = [[int(x) for x in input().split(" ")] for _ in range(N)]

  ans = 0
  for i in range(N-1):
    for j in range(i+1, N):
      x_i, y_i = X_Y[i]
      x_j, y_j = X_Y[j]
      if abs(x_i - x_j) >= abs(y_i - y_j):
        ans+=1

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
