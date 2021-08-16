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
        input = """2 3 1"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 0 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1000000 1000000 1000000"""
        output = """192151600"""
        self.assertIO(input, output)

def resolve():
  mod = 10**9+7
  # 順列総数。
  # カタラン数
  # http://www.geisya.or.jp/~mwm48961/kou3/onajimono1.htm
  # DP で解く?
  # N == K だったら単純な並び替えで解ける。
  # K == N-1 の時、初手連続で W を N 個置く場合 (1パターン) だけが条件を満たさない。
  # K == N-2 の時、初手連続で W を N-1 個置く場合と N-1 個のうちどれかが黒で、
  # ダメパターンを計算していくと良さそう。
  N, M, K = map(int, input().split(" "))
  if N > M+K:
    print(0)
    return

  def comb(N, R, mod):
    if N-R < R:
      R = N-R
    ans = 1
    for n in range(N-R+1, N+1):
      ans*=n
      if ans > mod: ans%=mod
    den = 1
    for r in range(2, R+1):
      den*=r
      if den > mod: den%=mod
    ans *= pow(den, mod-2, mod)
    return ans

  # 総数。
  ans = comb(N+M, N, mod)

  # 白を一個以上余らせて同数を作るパターンが何パターンあるかを考える。
  if N+M >= M+K+1:
    diff = comb(N+M, M+K+1, mod)
    ans -= diff
  print(ans%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
