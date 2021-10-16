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
        input = """3 2 1"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """100 100 0"""
        output = """73074801"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """60522 114575 7559"""
        output = """479519525"""
        self.assertIO(input, output)

def resolve():
  # 隣り合うブロックの組であって同じ色で塗られている組の個数が k (0 ~ K) 個であることを考える。
  # k 個の組が同じ色である場合、組の片方の色は自動的に決まるため、comb(N-1, k)*M*pow(M-1, N-k, mod) となる。
  # これを全て足し合わせれば良い。
  # そのままだと TLE するので、組み合わせ計算の連続性を使って高速化する。
  # 小定理を使えば早そう。
  mod = 998244353
  N, M, K = map(int, input().split(" "))

  ans = 0
  comb = 1
  for k in range(K+1):
    val = M*pow(M-1, N-k-1, mod)*comb
    ans += val
    if ans >= mod: ans%=mod

    comb *= (N-1-k)*pow(k+1, mod-2, mod)
    if comb>= mod: comb%=mod

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()