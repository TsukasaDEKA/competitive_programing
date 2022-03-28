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
        input = """3 4"""
        output = """13"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """20 30"""
        output = """71166"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """200000 200000"""
        output = """835917264"""
        self.assertIO(input, output)

def resolve():
  # 単純に dp をやると間に合わないので高速化する。
  # dp じゃないのでは？
  # (M+1)//2 < A[1] <= M の時、場合数は 1
  # (M+2)//3 < A[1] <= (M+1)//2 の時、場合数は N (A[2~N] のどこかで 1 回 2*A[1] へ遷移する or 1 回も遷移しない)
  # (M+3)//4 < A[1] <= (M+2)//3 の時、場合数は 2*(N-1)+1 (A[2~N] のどこかで 1 回 (2or3)*A[1] へ遷移する or 1 回も遷移しない)
  # (M+4)//5 < A[1] <= (M+3)//4 の時、場合数が複雑・・・ (N-1)C2 + 3*(N-1)C1 + 1・・・？一般化できそう。
  # (M+5)//6 < A[1] <= (M+4)//5 の時、場合数は (N-1)C2 + 4*(N-1)C1 + 1
  # (M+6)//7 < A[1] <= (M+5)//6 の時、場合数は 2=>4, 2=>6, 3=>6 遷移、2~6 遷移、遷移無しを考えて、 3*(N-1)C2 + 5*(N-1)C1 + 1
  # (M+7)//8 < A[1] <= (M+6)//7 の時、場合数は 2=>4, 2=>6, 3=>6 遷移、2~7 遷移、遷移無しを考えて、 3*(N-1)C2 + 6*(N-1)C1 + 1
  # (M+8)//9 < A[1] <= (M+7)//8 の時、場合数は 2=>4=>8 遷移、2=>4, 2=>6、3=>6, 4=>8 遷移、2~7 遷移、遷移無しを考えて、 (N-1)C3 + 4*(N-1)C2 + 6*(N-1)C1 + 1
  # ...
  # (M+K)//(K+1) < A[1] <= (M+(K-1))//K の時、・・・と進めていける。
  # 遷移の最大数は min(int(logM), N) になる。
  # 0 <= x <= min(int(logM), N-1) の x に関して、(N-1)Cx のそれぞれの個数を求めて集計すれば良さそう。
  # N-1 < int(logM) の時は場合分けがめんどくさそうなので、N, M が小さい時は DP で解く。
  # N 方向の遷移制限が無い前提で解けば良さそう。
  # 0 <= x <= int(logM) 
  from collections import defaultdict
  def get_min_prime_factor(n):
    prime_factors = list(range(n+1))
    prime_factors[0] = prime_factors[1] = 1
    for i in range(2, int(-(-n**0.5//1))+1):
      if prime_factors[i] == i:
        for j in range(i*i, n+1, i):
          if prime_factors[j] == j: prime_factors[j] = i
    return prime_factors

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

  mod = 998244353
  N, M = map(int, input().split(" "))
  if False:
    dp = [1]*(M+1)
    for n in range(N-1):
      for m in reversed(range(1, M+1)):
        for k in reversed(range(2*m, M+1, m)):
          dp[k] += dp[m]
          if dp[k] >= mod: dp[k]%=mod
    print(sum(dp[1:])%mod)
  else:
    # 最小素因数のテーブルを作成する。
    min_prime_factor = get_min_prime_factor(M)
    # comb 計算のキャッシュを持っておく。
    comb_cache = [None]*20
    ans = 0
    for m in range(1, M+1):
      temp_m = m
      # 素因数分解する。
      # 2**15 > 2*(10**5) なので最大 14 回程度の計算
      prime_count = defaultdict(int)
      while min_prime_factor[temp_m] != 1:
        prime_count[min_prime_factor[temp_m]]+=1
        temp_m//=min_prime_factor[temp_m]
      
      temp_ans = 1
      for v in prime_count.values():
        if comb_cache[v] is None:
          comb_cache[v] = comb_mod(v+N-2, v, mod)
        temp_ans*=comb_cache[v]
        if temp_ans>=mod: temp_ans%=mod

      temp_ans*=M//m
      if temp_ans>=mod: temp_ans%=mod

      ans+=temp_ans
      if ans>=mod: ans%=mod
    print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()