from itertools import count
import sys
from io import StringIO
from types import CodeType
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
5
#.#
...
..#"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
2
#.
.#"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8
8
........
........
........
........
........
........
........
........"""
        output = """64678"""
        self.assertIO(input, output)



def resolve():
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]

  from collections import deque
  popcnt = lambda x: bin(x).count("1")

  # 制約がものすごく小さい。
  # 64 bit で表現できる。
  N = int(input())
  K = int(input())
  field = [[x=="." for x in list(input())] for _ in range(N)]

  ans = set()
  checked = set()
  nexts = deque()
  for h in range(N):
    for w in range(N):
      if not field[h][w]: continue
      # bfs
      nexts.append((1<<(N*h+w)))

  while nexts:
    current_status = nexts.pop()

    if popcnt(current_status) == K:
      ans.add(current_status)
      continue

    for h_ in range(N):
      for w_ in range(N):
        if not field[h_][w_]: continue
        if current_status + (1<<(N*h_+w_)) in checked: continue
        if (current_status>>(N*h_+w_))&1: continue
        for i in range(4):
          h_n = h_+dh[i]
          w_n = w_+dw[i]
          if h_n < 0 or h_n >= N or w_n < 0 or w_n >= N: continue
          if not field[h_n][w_n]: continue
          if (current_status>>(N*h_n+w_n))&1:
            nexts.append(current_status + (1<<(N*h_+w_)))
            checked.add(current_status + (1<<(N*h_+w_)))
            break

  print(len(ans))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()