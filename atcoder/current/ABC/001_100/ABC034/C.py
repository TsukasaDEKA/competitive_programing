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
        input = """4 3"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """123 456"""
        output = """210368064"""
        self.assertIO(input, output)

def resolve():
  mod = 10**9+7
  # O(N**2) だと 101 点は無理。
  # なんか対称性を利用した解き方がありそう。
  # 解説 AC
  # 移動回数を考えると上方向に H-1 回、右方向に W-1 回移動して、その順番は自由。
  # そのことから、この問題の答えは
  # これは、H-1 個の上方向の移動と W-1 個の右方向の移動の順番を並べ替えて生じる組み合わせ数と考えることができる。
  # なので、 (H+W-2)C(H-1) が移動の通り数になる。
  mod = 10**9+7
  W, H = map(int, input().split(" "))
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

  print(comb_mod(H+W-2, H-1, mod))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()