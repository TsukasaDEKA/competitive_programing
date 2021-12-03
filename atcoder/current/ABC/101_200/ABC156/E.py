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
        input = """3 2"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """200000 1000000000"""
        output = """607923868"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """15 6"""
        output = """22583772"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  def comb_mod(n,r,mod):
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

  mod = 10**9+7
  # K >= N-1 の時、明らかに全ての組み合わせが可能である。
  # => 任意のマスに遷移する時に任意のマスへの遷移を中継すれば自由に遷移先を制御できるため。
  # その場合、その場合、N 人の人と N-1 枚の仕切りを自由に並べる方法を計算すれば良い。 => N+(N-1)CN
  # K < N-1 の場合が問題になる。
  # 2 <= K なので、全てが 1 のケースを作れない場合は存在しない。
  # K = N-2 の場合、１つに集合させるケースが作れなくなる。
  # N 個のの中から集合させる 1 つを選ぶのは NC1 になる。
  # また、N 人をその集合させる 1 つに人を割り振る選び方の中で、最低 1 個を割り振る方法は
  # (N-1+(1-1))C(1-1) となるので、
  # よって、N+(N-1)CN - (NC1)*(N-1+(1-1))C(1-1) となる。
  # これを一般化すると、
  # K = N-1-x の場合、作れなくなるケースは
  # (NC1)*(N-1+(1-1))C(1-1) + (NC2)*(N-2+(2-1))C(2-1) + ... + (NCx)*(N-x+(x-1))C(x-1) 個になる。
  # これを計算していけば良い。
  # comb の計算が重いのでメモ化とかが必要かも。
  N, K = map(int, input().split(" "))
  ans = comb_mod(2*N-1, N, mod)
  if K < N-1:
    X = N-1-K
    N_table = [1]*(X+1)
    N_1_table = [1]*(X+1)
    for x in range(1, X+1):
      N_table[x] = ((N_table[x-1]*(N-x+1))%mod)*pow(x, mod-2, mod)
      if N_table[x] < 0: N_table[x]%=mod
      if N_table[x] >= mod: N_table[x]%=mod

      N_1_table[x] = ((N_1_table[x-1]*(N-x))%mod)*pow(x, mod-2, mod)
      if N_1_table[x] < 0: N_1_table[x]%=mod
      if N_1_table[x] >= mod: N_1_table[x]%=mod

    for x in range(1, X+1):
      ans -= (N_table[x]*N_1_table[x-1])%mod
      if ans >= mod: ans %= mod
      if ans < 0: ans %= mod
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()