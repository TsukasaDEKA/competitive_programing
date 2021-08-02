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

    def test_入力例_1(self):
        input = """3 34
1
8 13 26"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 45
2
7 11 16 20 28 34 38"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 100
1
28 54 81"""
        output = """46"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3 100
2
28 54 81"""
        output = """26"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """20 1000
4
51 69 102 127 233 295 350 388 417 466 469 523 553 587 720 739 801 855 926 954"""
        output = """170"""
        self.assertIO(input, output)

def resolve():
  # できるだけ平均的に取りたい。
  # スコアは L//(K+1) 以下になるはず。
  # 長い方はいくら長くても大丈夫。
  # A の前後に 0 と L を入れると計算が楽そう。
  # 一切れあたりの羊羹の長さに変換してから考えるか？
  # 累積和を既に取ってあるような状態
  # 二分探索で L//(K+1) 以下の最大値を探るとどうだろう。
  # イマイチっぽい。
  # 射撃王みたいに「答え K を達成できるか？」で考える？
  # min(A) ~ L//(K+1) までの間に答えが必ずある。
  # トレランスも考えると計算量を減らせそう。
  # 例えば例 5 で答えが 200 になると仮定して計算すると、
  # 1000 - 200*5 = 0 なので、トレランス 0、つまり、全てが 200 丁度に分割できる必要がある。
  # 233 を選んだ場合、残り 764 を 4 分割するので、答えは764//4 = 191 以下になって、
  # 目標 を下回るのでやり直し。
  # 途中で実現可能かどうかを判定できるので、結構早くできるかも。
  N, L = map(int, input().split(" "))
  K = int(input())
  A = [0] + [int(x) for x in input().split(" ")] + [L]

  # メグル式二分探索。
  def binary_search(ok, ng, solve, k):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, k): ok = mid
      else: ng = mid
    return ok if solve(ok, k) else -1

  def solve(length, k):
    # 前から取っていって、長さ L 以上の羊羹が何個取れるか？を確認して、K 以上であれば良い。
    count = 0
    l = 0
    r = 0
    while r < len(A):
      while A[r] - A[l] < length:
        r+=1
        if r >= len(A): break
      else:
        count+=1
      l = r
    return count >= k+1

  ans = binary_search(1, L//2+1, solve, K)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
