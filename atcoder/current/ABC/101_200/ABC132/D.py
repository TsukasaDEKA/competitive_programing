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
        input = """5 3"""
        output = """3
6
1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2000 3"""
        output = """1998
3990006
327341989"""
        self.assertIO(input, output)

def comb_mod(n,r,mod):
  if n == r or r == 0:
    return 0
  if n-r<r:
    r=n-r
  N=n
  R=r
  u=1
  d=1
  for i in range(r):
    u*=N
    u%=mod
    N-=1
    d*=R
    d%=mod
    R-=1
  return u*pow(d,mod-2,mod)%mod

def resolve():
  # 青色のボールを i 個に分割する N-K 個のボールの置き方を考える。
  # 青ボールが K 個並べてあるとして、赤ボールを置ける場所を考える？
  # 青ボールが K 個ある場合、置ける場所は K+1 個 (両端も含む)
  # 青ボールを i 個に分割する場合、青ボールの間の K-1 個から i-1 個 (K-1 C i-1) を選択した上で、
  # 残った N-K-(i-1) 個の赤ボールを先程選んだ i-1 個の青ボールの間もしくは両端 (+2) のどこかに置く。(N-K-(i-1) + i-1 + 1 C i-1 + 1) => (N-K+1 C i)
  # (K-1 C i-1)*(N-K+1 C i)
  # factorial の計算が重いので注意する。
  mod = 10**9+7
  N, K = map(int, input().split(" "))
  for i in range(1, K+1):
    # 分割数 - 1 が赤ボールより多かったら、その分割は達成できないので 0 を出力
    if i-1 > N-K:
      print(0)
      continue
    print(comb_mod(K-1, i-1, mod)*comb_mod(N-K+1, i, mod)%mod)

resolve()

if __name__ == "__main__":
    unittest.main()
