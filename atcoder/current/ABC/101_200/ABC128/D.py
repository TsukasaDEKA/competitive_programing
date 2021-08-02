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
        input = """6 4
-10 8 2 1 2 6"""
        output = """14"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 4
-6 -100 50 -2 -5 -3"""
        output = """44"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6 3
-6 -100 50 -2 -5 -3"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # DP でできる？
  # N, K が少ないので、全探索すれば良さそう。
  # 一旦左右から K 個取り出して、最後にまとめて負の価値の宝石を返す動作をする。
  # 途中で返しても邪魔になるだけ。
  # 累積和と i 番目の宝石を取った場合に手元に存在する宝石をソートされた状態で持っておくと、
  # 毎回計算するときに楽になる。
  # N < K の時に注意する。
  # 丁度 K 回ではなく、K 回「まで」なので、途中で切り上げても良い。
  # 左から L 個、右から R 個取った時に、L+R <= min(N, K) であれば実行できる。
  # 雑に実装しても間に合いそう。

  N, K = map(int, input().split(" "))
  V = [int(x) for x in input().split(" ")]

  minus_l = [[] for _ in range(N+1)]
  minus_r = [[] for _ in range(N+1)]
  for i in range(N):
    if V[i] < 0:
      for j in range(i, N):
        minus_l[j+1].append(V[i])
    if V[N-i-1] < 0:
      for j in range(i, N):
        minus_r[j+1].append(V[N-i-1])

  ans = 0
  for l in range(min(N, K)+1):
    for r in range(min(N-l, K-l)+1):
      val = sum(V[:l]) + sum(V[N-r:])
      if K - l - r < 0: continue
      if K - l - r == 0:
        ans = max(ans, val)
        continue
      if len(minus_l[l])+len(minus_r[r]) <= K - l - r:
        # もし残り回数よりもマイナスの宝石が少なかった場合、全部返却する。
        val -= sum(minus_l[l]) + sum(minus_r[r])
      else:
        # 小さい方から返却する。
        val -= sum(sorted(minus_l[l] + minus_r[r])[:K-l-r])
      ans = max(ans, val)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
