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
        input = """2 3
--o
o--"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 4
-o--
----
----
----
-o--"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  H, W = map(int, input().split(" "))
  S = [list(input()) for _ in range(H)]

  x_s, y_s = -1, -1
  x_g, y_g = -1, -1
  for h in range(H):
    for w in range(W):
      if S[h][w] == "o":
        if x_s == -1:
          x_s, y_s = h, w
        else:
          x_g, y_g = h, w

  print(abs(x_s-x_g) + abs(y_s-y_g))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()