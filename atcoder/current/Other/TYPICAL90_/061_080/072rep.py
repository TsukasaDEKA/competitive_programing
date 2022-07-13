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
...
.#.
..."""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 6
......"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 4
....
#...
....
...#"""
        output = """12"""
        self.assertIO(input, output)

def resolve():
  popcnt = lambda x: bin(x).count("1")
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]
  from collections import deque

  # 盤面の状態を 16 bit の変数で渡しながら DFS
  inf = 10**18+1
  H, W = map(int, input().split(" "))
  C = [list(input())+["#"] for _ in range(H)] + [["#"]*(W+1)]

  ans = -1
  nexts = deque()
  for h_s in range(H):
    for w_s in range(W):
      if C[h_s][w_s] == "#": continue
      nexts.append((h_s, w_s, 1<<(W*h_s+w_s)))
      while nexts:
        h, w, status = nexts.pop()
        # print(nexts)
        for i in range(4):
          h_ = h+dh[i]
          w_ = w+dw[i]
          if C[h_][w_] == "#": continue
          if (h_s, w_s) == (h_, w_):
            k = popcnt(status)
            if k >= 3:
              ans = max(ans, k)
            continue
          if status&(1<<(W*h_+w_)): continue
          nexts.append((h_, w_, status|(1<<(W*h_+w_))))

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()