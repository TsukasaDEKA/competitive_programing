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
        input = """2 5
0 1 0 1 0
1 0 0 0 1"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 6
1 0 0 0 1 0
1 1 1 0 1 0
1 0 1 1 0 1"""
        output = """15"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  H, W = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(H)]
  COUNT = [0]*W
  for i in range(H):
    for j in range(W):
      if A[i][j]:
        COUNT[j] += 1
  
  ans = 0
  # b: 二進数表記にした時に i 桁目が 1 だったら i 行目をひっくり返す。
  for b in range(1<<H):
    # ひっくり返す行インデックスのリスト
    tar = [i for i in range(H) if b&(1<<i)]

    # count[i]: ひっくり返す行の i 列目に含まれる裏返っているせんべいの枚数。
    count = [0]*W
    for t in tar:
      for i in range(W):
        if A[t][i]:
          count[i] += 1

    # 元の列に含まれる裏返った煎餅が COUNT[i] 枚だとすると、対象となる行を全てひっくり返した時点で
    # COUNT[i] - count[i] + (len(tar) - count[i]) 枚の煎餅が裏返った状態になる。
    # i 列の裏返った煎餅が X 枚だとすると、その列を裏返す操作した時、H-X 枚の煎餅が裏返った状態になる。
    # つまり、裏返った煎餅の枚数を最大化したい時、max(X, H-X) になるように操作をすれば良いので、
    # 全ての列に対して max(X, H-X) の合計をとる。
    temp = 0
    for i in range(W):
      X = COUNT[i]+len(tar)-2*count[i]
      temp += max(X, H-X)
    ans = max(ans, temp)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()