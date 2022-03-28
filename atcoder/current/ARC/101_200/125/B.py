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
        input = """3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10000000000"""
        output = """52583544"""
        self.assertIO(input, output)


def resolve():
  def count_square(ok, ng, base_x, n):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if mid*(2*base_x-mid) <= n: ok = mid
      else: ng = mid

    return ok

  def find_x(ok, ng, k, n):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if k*(2*mid-k) <= n: ok = mid
      else: ng = mid

    return ok

  mod = 998244353
  # 平方数は 1, 4, 9・・・
  # x**2 <= N の時、y を調整することで x**2 未満の平方数は全て実現可能。
  # つまり、 x <= sqrt(N) の場合は線形で個数が増える。=> x*(x+1)//2
  # x > sqrt(N) の場合、x**2-N ~ x**2-1 の範囲に含まれる平方数の個数を求める。これは二分探索で簡単に求まる
  # => x**2-N ~ x**2-1 の範囲に含まれる平方数の個数は 0 ~ x 個の間に存在するはずである。
  # 全ての x に対してこれを行うと TLE する。
  # 同じ個数の平方数を持つ x が何個あるかを二分探索で求めることにする。
  # まず、x' まで答えがわかっているとする。l = x'+1 と置いた時、
  # 上記のことから l**2-N ~ l**2-1 に含まれる平方数が分かる。これを k とする。
  # 平方数が k 個含まれる最大の x (= r) を求めたい。
  # 含まれる平方数は x の増加に伴い広義単調減少するので二分探索で求められる。
  # 今、k*(r-l+1) 個の x, y の組み合わせが見つかった。
  # 次に r+1 = l とおいて上記の処理を繰り返す。
  N = int(input())

  ans = 0
  # x <= sqrt(N) の範囲分の答えを求める。
  x = int(-(-(N**0.5)))
  ans += (x+1)*x//2

  r = x
  while True:
    l = r+1
    # l**2-N ~ l**2-1 に含まれる平方数の個数を求める
    ok = 0
    ng = l+1
    k = count_square(ok, ng, l, N)
    # 平方数の個数が 0 の場合計算を終了する。
    if k == 0:
      print(ans)
      break
    
    ok = l
    ng = N+1
    # 平方数の個数が k 個になる最大の x を求める。
    r = find_x(ok, ng, k, N)
    ans+=k*(r-l+1)
    ans%=mod

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()