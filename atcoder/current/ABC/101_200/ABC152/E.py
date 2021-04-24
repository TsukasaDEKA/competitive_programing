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
        input = """3
2 3 4"""
        output = """13"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
12 12 12 12 12"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
1000000 999999 999998"""
        output = """996989508"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5
1 2 3 4 5"""
        output = """137"""
        self.assertIO(input, output)

def resolve():
  from math import gcd
  # 合計値なので、B そのものを出力するわけでは無い。
  # N <= 10**4 がなんか中途半端な感じがする。
  # 最大公約数で割った値を入れる。
  # 例 1 [2, 3, 4]で考えてみる。
  # gcd(2, 3) = 1 なので、B[0] = A[1]/1 = 3、B[1] = A[0]/1 = 2
  # gcd(6, 4) = 2 なので、B[1] = B[1]*A[2]/2 = 4, B[2] = B[1]*A[1]/2 = 3
  # ここで、 B[1] に 2 を掛けたので、B[:1] 全体にも 2 を掛けないと辻褄が合わなくなる。
  # ただ、毎回全体に掛けてると計算量が大きくなってしまうので、累積和を取っておく必要がある。
  # どのような i, j についてもだった。
  # 最小公倍数を求めて、フェルマーの小定理でいい感じにする。
  mod = 10**9+7
  from math import gcd
  from functools import reduce
  def lcm_base(x, y):
    return (x * y) // gcd(x, y)
  def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

  N = int(input())
  A = [int(x) for x in input().split(" ")]

  LCM_A = lcm(*A)
  ans = 0
  for i in range(N):
    ans += LCM_A*pow(A[i], mod-2, mod)
    if ans >= mod: ans%=mod
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
