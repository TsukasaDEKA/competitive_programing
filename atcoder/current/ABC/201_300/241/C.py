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
        input = """8
........
........
.#.##.#.
........
........
........
........
........"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
######
######
######
######
######
######"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
..........
#..##.....
..........
..........
....#.....
....#.....
.#...#..#.
..........
..........
.........."""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [[x for x in list(input())] for _ in range(N)]

  for i in range(N):
    for j in range(N):
      # 右
      count = 0
      for j_ in range(j, j+6):
        if j_ >= N: break
        if A[i][j_] != "#":
          count += 1
      else:
        if count <= 2:
          print("Yes")
          return

      # 下
      count = 0
      for i_ in range(i, i+6):
        if i_ >= N: break
        if A[i_][j] != "#":
          count += 1
      else:
        if count <= 2:
          print("Yes")
          return

      # 右下
      count = 0
      for d in range(6):
        i_ = i+d
        j_ = j+d
        if i_ >= N or j_ >= N: break
        if A[i_][j_] != "#":
          count += 1
      else:
        if count <= 2:
          print("Yes")
          return

      # 左下
      count = 0
      for d in range(6):
        i_ = i+d
        j_ = j-d
        if i_ >= N or j_ < 0: break
        if A[i_][j_] != "#":
          count += 1
      else:
        if count <= 2:
          print("Yes")
          return

  print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()