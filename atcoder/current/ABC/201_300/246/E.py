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
1 3
3 5
....#
...#.
.....
.#...
#...."""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
3 2
4 2
....
....
....
...."""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """18
18 1
1 18
..................
.####.............
.#..#..####.......
.####..#..#..####.
.#..#..###...#....
.#..#..#..#..#....
.......####..#....
.............####.
..................
..................
.####.............
....#..#..#.......
.####..#..#..####.
.#.....####..#....
.####.....#..####.
..........#..#..#.
.............####.
.................."""
        output = """9"""
        self.assertIO(input, output)

def resolve():
  dh = [-1, -1,  1, 1]
  dw = [-1,  1, -1, 1]

  from collections import deque

  # 斜めに移動する。
  inf = 10**18+1
  N = int(input())
  A = [int(x)-1 for x in input().split(" ")]
  B = [int(x)-1 for x in input().split(" ")]
  # if sum(A)%2 != sum(B)%2:
  #   print(-1)
  #   return
  FEILD = [list(input())+["#"] for _ in range(N)] + [["#"]*(N+1)]
  checked = [[False]*N for _ in range(N)]
  checked[A[0]][A[1]] = 3
  step = [[-1]*N for _ in range(N)]
  step[A[0]][A[1]] = 0

  nexts = deque()
  nexts.append((A))
  while nexts:
    h, w = nexts.popleft()
    for i in range(4):
      dir = 1 if dh[i]*dw[i] > 0 else 2
      h_ = h
      w_ = w
      while True:
        h_ += dh[i]
        w_ += dw[i]
        if FEILD[h_][w_] == "#": break
        if checked[h_][w_]&dir: break
        checked[h_][w_] += dir

        if step[h_][w_] >= 0: continue

        step[h_][w_] = step[h][w]+1
        nexts.append((h_, w_))

  # print(*step, sep="\n")
  print(step[B[0]][B[1]])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()