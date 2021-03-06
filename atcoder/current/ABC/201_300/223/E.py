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
        input = """3 3 2 2 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3 4 4 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1000000000 1000000000 1000000000000000000 1000000000000000000 1000000000000000000"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  from itertools import permutations

  # 考える必要のある分割パターンは 4 種類。
  # A、B、C の並びも全種類試すべき？それでも 4*6 = 24 種類。
  X, Y, A, B, C = map(int, input().split(" "))

  for a, b, c in permutations([A, B, C], 3):
    for x, y in [[X,Y], [Y,X]]:
      x -= (a+y-1)//y
      if x <= 0: continue

      for x_, y_ in [[x,y], [y,x]]:
        x_ -= (b+y_-1)//y_
        if x_*y_ >= c:
          print("Yes")
          return

  print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()