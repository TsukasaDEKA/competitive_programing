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

    def test_入力例1(self):
        input = """3 4
4 6 2 5
3 5 6 7
2 5 5 6"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """2 2
4 0
7 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """2 3
0 0 0
1 2 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """3 3
1 2 3
6 5 4
7 8 9"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """1 5
0 1 2 3 4"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  # 二次元累積和で解けそう。
  # H, W <= 100 なので、
  # その内 xi < xj と yi < yj を満たす 2 点を選ぶとすると
  #  (100C2)**2 = 24502500 なのでギリギリ間に合うか？
  H, W = map(int, input().split(" "))
  C = [list(map(int, input().split(" "))) for _ in range(H)]
  INT_C = [[0]*(W+1) for _ in range(H+1)]
  # WHITE = [[0]*(W+1) for _ in range(H+1)]
  # BLACK = [[0]*(W+1) for _ in range(H+1)]
  for h in range(H):
    INT_C_h = INT_C[h]
    INT_C_h_p1 = INT_C[h+1]
    for w in range(W):
      INT_C_h_p1[w+1] = INT_C_h[w+1] + INT_C_h_p1[w] - INT_C_h[w]
      if (h+w)%2: INT_C_h_p1[w+1] += C[h][w]
      else: INT_C_h_p1[w+1] -= C[h][w]

  ans = 0
  for hi in range(H):
    INT_C_hi = INT_C[hi]
    for hj in range(hi+1, H+1):
      INT_C_hj = INT_C[hj]
      for wi in range(W):
        INT_C_hi_wi = INT_C_hi[wi]
        INT_C_hj_wi = INT_C_hj[wi]
        for wj in reversed(range(wi+1, W+1)):
          if INT_C_hj[wj] - INT_C_hj_wi - INT_C_hi[wj] + INT_C_hi_wi == 0 and ans < (hj-hi)*(wj-wi):
            ans = (hj-hi)*(wj-wi)
            break
  else:
    print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
