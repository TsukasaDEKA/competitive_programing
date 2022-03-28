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
...
..."""
        output = """132
313
541"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 7
1.2.3.4
.5.1.2.
3.4.5.1
.2.3.4.
5.1.2.3"""
        output = """1425314
2531425
3142531
4253142
5314253"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 1
."""
        output = """4"""
        self.assertIO(input, output)

dh = [-1, 0, 1, 0]
dw = [0, -1, 0, 1]

def resolve():
  inf = 10**18+1
  H, W = map(int, input().split(" "))
  FIELD = [list(input()) for _ in range(H)]

  # ans = [["."]*W for _ in range(H)]
  for h in range(H):
    for w in range(W):
      if FIELD[h][w] == ".":
        used = set()
        for i in range(4):
          h_ = h+dh[i]
          w_ = w+dw[i]
          if h_ < 0 or h_ >= H or w_ < 0 or w_ >= W: continue
          if FIELD[h_][w_] == ".": continue
          used.add(FIELD[h_][w_])
        
        for i in range(1, 6):
          if str(i) in used: continue
          FIELD[h][w] = str(i)
          break
  
  for f in FIELD:
    print("".join(f))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()