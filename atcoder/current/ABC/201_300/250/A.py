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
        input = """3 4
2 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 4
1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 4
3 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1 10
1 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """8 1
8 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_6(self):
        input = """1 1
1 1"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]

  inf = 10**18+1
  H, W = map(int, input().split(" "))
  R, C = [int(x)-1 for x in input().split(" ")]
  table = [[1]*W+[0] for _ in range(H)] + [[0]*(W+1)]
  ans = 0
  for i in range(4):
    h = R+dh[i]
    c = C+dw[i]
    ans += table[h][c]

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()