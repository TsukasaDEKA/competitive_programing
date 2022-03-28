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
        input = """4 5 3
8
7
4
2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 10 4
20
20"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 2 1
900000000
900000000
1000000000
1000000000
1000000000"""
        output = """800000000"""
        self.assertIO(input, output)

def resolve():
  # メグル式二分探索。
  def binary_search(ok, ng, solve, H, A, B):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, H, A, B): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok

  def solve(x, H, A, B):
    count = 0
    for h in H:
      count+=max(0, (h-x*B+A-B-1)//(A-B))

    return count <= x

  # 答えは明らかに maxH/A ~ maxH/B (切り上げ) の間にある。
  # 答えで二分探索して、答えを X とした時に、魔物を全滅させることができるかどうかを O(N) で計算できれば良い。
  # 魔物 i に対して A, B それぞれを使う回数を a_i, b_i とした時に、
  # a_i+b_i = X で、 a_i*A + b_i*B >= Hi を満たす最小の a_i は
  # a_i = ((Hi-X*B)+A-B-1)//(A-B) で求められる。
  # この時、a_i が負、もしくは b_i が負になるならば X は答えではない。
  # X -= a_i とし、同じことを各魔物にやっていけば良さそう。
  N, A, B = map(int, input().split(" "))
  H = sorted([int(input()) for _ in range(N)], reverse=True)
  print(binary_search(max(H), 0, solve, H, A, B))

import sys
sys.setrecursionlimit(500*500)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()