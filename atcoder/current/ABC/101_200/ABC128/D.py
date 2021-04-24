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

#     def test_Sample_Input_1(self):
#         input = """6 4
# -10 8 2 1 2 6"""
#         output = """14"""
#         self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 4
-6 -100 50 -2 -5 -3"""
        output = """44"""
        self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """6 3
# -6 -100 50 -2 -5 -3"""
#         output = """0"""
#         self.assertIO(input, output)

def resolve():
  # DP でできる？
  # N, K が少ないので、全探索すれば良さそう。
  # 一旦左右から K 個取り出して、最後にまとめて負の価値の宝石を返す動作をする。
  # 途中で変換しても邪魔になるだけ。
  # 累積和と i 番目の宝石を取った場合に手元に存在する宝石をソートされた状態で持っておくと、
  # 毎回計算するときに楽になる。
  # N < K の時に注意する。

  N, K = map(int, input().split(" "))
  V = [int(x) for x in input().split(" ")]

  minus_l = [[] for _ in range(N)]
  minus_r = [[] for _ in range(N)]
  for i in range(N):
    if V[i] < 0:
      for j in range(i, N):
        minus[j].append(V[i])

  for i in range(N):
    minus[i].sort()
  print(minus)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
