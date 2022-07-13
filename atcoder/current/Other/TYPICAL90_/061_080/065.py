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
        input = """3 1 2 5
4 2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """65 6 12 35
30 18 35"""
        output = """257190020"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """23502 65936 72385 95835
72759 85735 72385"""
        output = """229429276"""
        self.assertIO(input, output)

def resolve():
  # R, G, B からそれぞれ何個取るかを r, g, b と置く。
  # r, g, b をそれぞれ決めた時にそれが何通りあるかは RCr * GCg * BCb になる。
  # RCr, GCg, BCb は割と重い計算なので、事前にそれぞれの r, g, b について RCr, GCg, BCb を計算しておく。
  # r, g, b が取りうる値の範囲について、制約がある。
  # 例 1 だと r = [3:3], g = [1:1], b = [1:1] となる。
  # この制約は式変形で得られる。
  # r と g を決めたら b は自動的に決まる。
  # r と g の組み合わせを全探索してしまうと TLE するのでここから計算量を下げる工夫が必要。
  # わからないので R, G, B <= 3000 について WA しないか確認する。(上記の制約の他にも制約がありそう。)
  # まとめて計算できる部分はないか考える。

  # 0 <= r <= N の範囲で nCr のリストを返す。
  # 逆元を使っているので mod が素数かつ n より大きくないと変な動きするかも
  def nCr_list(N, mod):
    comb = [1]*(N+1)
    comb[1] = comb[N-1] = N
    for r in range(2, N//2+1):
      diff = (N-r+1)*pow(r, mod-2, mod)%mod
      comb[r] = comb[N-r] = (comb[r-1]*diff)%mod
    return comb

  mod = 998244353
  R, G, B, K = map(int, input().split(" "))
  X, Y, Z = map(int, input().split(" "))

  comb_R = nCr_list(R, mod)
  comb_G = nCr_list(G, mod)
  comb_B = nCr_list(B, mod)

  ans = 0
  for r in range(K-Y, min(R, X, Z)+1):
    for g in range(K-Z, min(G, X-r, Y)+1):
      temp = comb_R[r]
      b = K-r-g
      if r+b > Z or g+b > Y: continue
      if b < K-X: continue
      if b > B: continue

      # print(r, g, b, r+g+b, r+g, g+b, b+r)
      temp *= comb_G[g]
      if temp > mod: temp%=mod
      temp *= comb_B[b]
      if temp > mod: temp%=mod

      ans += temp
      if ans > mod: ans%=mod
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
