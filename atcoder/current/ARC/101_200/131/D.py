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

#     def test_Sample_Input_1(self):
#         input = """3 3 3
# 0 2 7 9
# 100 70 30"""
#         output = """270"""
#         self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3 8
0 2 7 9
100 70 30"""
        output = """200"""
        self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """7 5 47
# 0 10 40 100 160 220
# 50 25 9 6 3"""
#         output = """111"""
#         self.assertIO(input, output)

#     def test_Sample_Input_4(self):
#         input = """100 1 5
# 0 7
# 100000000000"""
#         output = """300000000000"""
#         self.assertIO(input, output)

#     def test_Sample_Input_5(self):
#         input = """15 10 85
# 0 122 244 366 488 610 732 854 976 1098 1220
# 10 9 8 7 6 5 4 3 2 1"""
#         output = """119"""
#         self.assertIO(input, output)

def resolve():
  from bisect import bisect_left
  # まず、矢は間隔 D で打つのが最適である (多分)

  # 一本目を R[1] に打つのが最適？=> 例 2 を見る限りそんなことはない。
  # 一本目を X に打った時に

  # 矢を最大本数かつ D の間隔で打つ時、右端の矢の動かせる範囲は (R[1]-(2*R[1])%D) ~ R[1] の間である。
  # この状態で次は S[1] を取れるエリアに打てる矢の最大本数を求める。
  # 1 本目の矢の位置を X とした場合、[-R[2], -R[1]), (R[1], R[2]] の範囲に入る矢の本数は、
  # ((R[2]-X)//D-(R[1]-X)//D) + (R[2]+X)//D - (R[1]+X)//D
  # = (R[2]-R[1]+R[2]-R[1])//D
  # = 2*(R[2]-R[1])//D で与えられる・・・X の位置に依存しない？？？？

  N, M, D = map(int, input().split(" "))
  R = [int(x) for x in input().split(" ")]
  S = [int(x) for x in input().split(" ")]

  ans = S[0]
  r = R[1]+D
  l = R[1]-D
  for i in range(N-1):
    r_i = bisect_left(R, r)
    if r_i == len(R):
      r_score = 0
    else:
      r_score = S[r_i-1]

    l_i = bisect_left(R, abs(l))
    if l_i == len(R):
      l_score = 0
    else:
      l_score = S[l_i-1]

    if r_score == l_score:
      if r > abs(l): target = "l"
      else: target = "r"

    elif r_score > l_score: target = "r"
    else: target = "l"

    print(r_score, r, l_score, l, ans)
    if target == "r":
      ans += r_score
      r += D
    else:
      ans += l_score
      l -= D

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()