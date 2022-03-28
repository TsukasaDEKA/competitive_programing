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
        input = """10 10
3 3 3
2 1 1
5 2 3
1 5 6
2 9 3
4 6 12
11 18 5
4 15 25
0 2 3
1 1 7
0 1
0 2
0 10
3 10
0 100
3 8
1 5
2 9
3 4
6 9"""
        output = """8.843002
80.992182
4173.878112
3865.997282
8512.668894
2882.971997
1227.377293
3629.490541
114.081013
1747.545749"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 5
5 10 10
4 100 100
3 1000 1000
2 1000 1000
1 1000 1000
0 3
2 1000
4 314
3 217
5 432"""
        output = """9409079.422279
3139502408.531295
2100737789.465234
1613523459.243475
2532621914.444282"""
        self.assertIO(input, output)

def resolve():
  # 参考: 円錐の切り取り https://mathwords.net/ensuidai
  # 単純にめんどくさい。
  from math import pi
  N, Q = map(int, input().split(" "))
  S = [[int(x) for x in input().split(" ")] for _ in range(N)]

  for _ in range(Q):
    A, B = [int(x) for x in input().split(" ")]
    ans = 0.0
    for x, r, h in S:
      # 範囲が重複しない場合は飛ばす。
      if A >= x+h or B <= x: continue

      # 円錐の範囲よりも大きいと不便なので制約をかける
      A_, B_ = max(A, x), min(B, x+h)

      # 断面の円の半径と断面間の距離
      r_1 = ((h-A_+x)*r)/h
      r_2 = ((h-B_+x)*r)/h
      h_ = B_-A_

      # 体積を計算
      ans += pi*h_*(r_1**2 + r_2**2 + r_1*r_2)/3
    print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()