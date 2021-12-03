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
        input = """3
1 2
3 6
7 4"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 2
2 2
4 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
0 0
0 1000000000
1000000000 0
1000000000 1000000000"""
        output = """8"""
        self.assertIO(input, output)

def resolve():
  # i の最小公倍数と j  の最小公倍数
  # N の個数が小さい
  # 高速に最大公約数を求めたい。
  # 拡張ユークリッドの互除法
  def extgcd(a, b):
    if b:
      g, y, x = extgcd(b, a % b)
      y -= (a // b)*x
      return g, x, y
    return a, 1, 0

  inf = 10**18+1
  N = int(input())
  ans = set()
  TOWNS = [[int(x) for x in input().split(" ")] for _ in range(N)]
  for i in range(N):
    x_i, y_i = TOWNS[i]
    for j in range(N):
      if i == j: continue
      x_j, y_j = TOWNS[j]
      dx, dy = x_i-x_j, y_i-y_j
      if dx == 0 or dy == 0:
        dx = dx//max(1, abs(dx))
        dy = dy//max(1, abs(dy))
      else:
        # print(dx, dy, extgcd(dx, dy))
        g, _, _ = extgcd(dx, dy)
        g = abs(g)
        if g == 0:
          # print(dx, dy)
          continue
        dx = dx//g
        dy = dy//g
      ans.add((dx, dy))

  print(len(ans))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()