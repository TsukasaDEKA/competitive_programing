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
        input = """1"""
        output = """1"""
        self.assertIO(input, output)


    def test_Sample_Input_2(self):
        input = """2"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  # 解説 AC
  # 正十二角形の内角は 150°。
  # これを正三角形と正方形で作ろうとすると、それぞれ一個ずつ使う必要がある。
  # 辺の長さが d の正十二角形を外側から埋めていく時の事を考える。
  # 例えば 1 つの辺を正三角形で埋めて、その隣の辺を正方形で埋める時
  # 内側にできる空間は十二角形 (六角形の場合もあるが、一旦考慮から外す) であり、
  # 正三角形で作られた辺が d-1、正方形で作られた辺が d となる。
  # また、正三角形と正方形を組み合わせないと 150°を作れないため、
  # d-1 になる辺と d となる辺は一個置きに作られる。
  # この状態遷移を再帰的に解いていけば良い。
  # d-1 = 0 となる場合について
  # d-1 = 0 となる場合、内側に作られる空間は正六角形になる。
  # 正六角形の内角は 120°であり、これは正三角形を 2 個使う必要がある。
  # また、内部に正方形を含むことはできない。
  # 以上のことにより、d-1 = 0 になった時点で置き方のパターン数は 1 になる。
  # 再帰だとメモリが辛いことになるので、深さ優先探索をしていく。=> 無理っぽい
  # 解説だと二項係数を使う。何故かはわからない。
  # 二項係数をいい感じに計算する必要がありそう。
  mod = 998244353
  d = int(input())
  ans = 1

  for i in range(d+1, 2*d+1):
    ans*=i
    if ans >= mod: ans%=mod
  
  for i in range(2, d+1):
    ans *= pow(i, mod-2, mod)
    if ans >= mod: ans%=mod

  print((ans*pow(2, mod-2, mod))%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
