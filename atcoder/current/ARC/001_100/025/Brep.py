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
4 6 2 5
3 5 6 7
2 5 5 6"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2
4 0
7 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2 3
0 0 0
1 2 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """3 3
1 2 3
6 5 4
7 8 9"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """1 5
0 1 2 3 4"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  # 白を負の数として扱い、二次元累積和を作って全区間試す。
  # それだと計算量が怪しい
  H, W = map(int, input().split(" "))
  FIELD = [[int(x) for x in input().split(" ")] for _ in range(H)]

  # 白マスだけ反転
  for h in range(H):
    for w in range(W):
      if (h+w)%2:
        FIELD[h][w] *= -1

  INTEGRA = [[0]*(W+1) for _ in range(H+1)]
  for h in range(H):
    INTEGRA_h = INTEGRA[h]
    INTEGRA_h_1 = INTEGRA[h+1]
    FIELD_h = FIELD[h]
    for w in range(W):
      INTEGRA_h_1[w+1] = INTEGRA_h[w+1]+INTEGRA_h_1[w]-INTEGRA_h[w]+FIELD_h[w]

  # print(*INTEGRA, sep="\n")
  ans = 0
  for h in range(H):
    INTEGRA_h = INTEGRA[h]
    for w in range(W):
      INTEGRA_hw = INTEGRA_h[w]
      for h_ in range(H, h, -1):
        INTEGRA_h_ = INTEGRA[h_]
        h_w_hw = INTEGRA_hw - INTEGRA_h_[w]
        for w_ in range(W, w, -1):
          temp = (w_-w)*(h_-h)
          if temp <= ans: break
          if INTEGRA_h_[w_] - INTEGRA_h[w_] + h_w_hw == 0:
            if temp > ans: ans = temp

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()