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
        input = """4 5
0 s 0 1
0 0 1 0
0 1 1 0
0 0 1 g
0 0 0 0"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 4
0 s 0 1
1 0 0 0
0 1 1 1
0 0 0 g"""
        output = """Fail"""
        self.assertIO(input, output)

def resolve():
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]

  from collections import deque

  inf = 10**18+1
  W, H = map(int, input().split(" "))
  FIELD = [input().split(" ")+["1"] for _ in range(H)]+[["1" for _ in range(W+1)]]

  Sh, Sw, Gh, Gw = None, None, None, None
  for h in range(H):
    for w in range(W):
      if FIELD[h][w] == "s":
        Sh, Sw = (h, w)
      if FIELD[h][w] == "g":
        Gh, Gw = (h, w)

  step = [[-1]*W for _ in range(H)]
  step[Sh][Sw] = 0
  nexts = deque([(Sh, Sw)])
  while nexts:
    h, w = nexts.popleft()
    for i in range(4):
      h_ = h+dh[i]
      w_ = w+dw[i]
      if FIELD[h_][w_] == "1": continue
      if step[h_][w_] >= 0: continue
      step[h_][w_] = step[h][w]+1
      nexts.append((h_, w_))
  print(step[Gh][Gw] if step[Gh][Gw] >= 0 else "Fail")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()