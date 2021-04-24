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
2 4 3"""
        output = """63"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
10"""
        output = """100"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
853983 14095 543053 143209 4324 524361 45154"""
        output = """206521341"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5
1 2 3 4 5"""
        output = """243"""
        self.assertIO(input, output)

def resolve():
  mod = 998244353
  # 全ての部分列なのでソートしても大丈夫
  # やっと理解した。
  # ソート後、A [0:i] を使って作ることのできる部分列の和を作る。
  # i をインクリメントする。
  # 例えば例 1 だと、
  # 2*(2+(2^0)*0)
  # + 3*(3+(2^0)*2)
  # + 4*(4+(2^0)*3+(2^1)*2) = 63
  N = int(input())
  A = sorted([int(x) for x in input().split(" ")])
  ans = 0
  mul = 0
  for a in A:
    ans += a*(a+mul)
    mul = (a+2*mul)
    if ans>=mod: ans%=mod
    if mul>=mod: mul%=mod
  print(ans)
resolve()

if __name__ == "__main__":
    unittest.main()
