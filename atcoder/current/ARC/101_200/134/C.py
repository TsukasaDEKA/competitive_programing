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
        input = """2 2
3 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 1
1 100"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """20 100
1073813 90585 41323 52293 62633 28788 1925 56222 54989 2772 36456 64841 26551 92115 63191 3603 82120 94450 71667 9325"""
        output = """313918676"""
        self.assertIO(input, output)

def resolve():
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
  # K が小さい。
  # 箱に入る個数が少ない順に考える。
  # 
  mod = 998244353
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  one = A[0]
  # ボールが 1 種類の時はそれを割り振る通り数を求める。
  if N == 1:
    print(comb_mod(one-1, K-1, mod))
    return
  
  # 1 のボール を全箱に 1 個づつ入れたあと、残ったボーエうがその他のボールの数よりも少なかったら 0 通り。
  others = A[1:]
  sum_others = sum(others)
  if one - K < sum_others:
    print(0)
    return

  # K 個数の箱に val 個のボールを好きに割り振る。
  ans = 1
  for val in others:
    ans *= comb_mod(val+(K-1), K-1, mod)
    if ans >= mod: ans%=mod

  # 残った 1 のボールを最低 1 個箱に入るように割り振る。
  ans *= comb_mod((one-sum_others)-1, K-1, mod)
  if ans >= mod: ans%=mod
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()