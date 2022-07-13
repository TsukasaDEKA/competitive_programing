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
BWR"""
        output = """W"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
RRBB"""
        output = """W"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
BWWRBW"""
        output = """B"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """8
WWBRBBWB"""
        output = """R"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """21
BWBRRBBRWBRBBBRRBWWWR"""
        output = """B"""
        self.assertIO(input, output)

def resolve():
  # 解説 AC
  # ["B", "W", "R"] をそれぞれ [0, 1, 2] とすると、
  # 二個のブロックの上に置くブロックの色を簡単に求めることができる。
  # 例：-(0+1)%3 = 2 

  # ここで、高さ N のピラミッドの頂点の色は。
  # N = 2 の時、 -(x_0+x_1)%3 
  # N = 3 の時、 -(x_0 + 2*x_1 + x_2)%3
  # N = 4 の時、 -(x_0 + 3*x_1 + 3*x_2 + x_3)%3 => -(x_0 + x_3)%3
  # ...
  # となる。
  # ここから考えていくと N-1 が 3 の倍数である時、頂点の色は以下の式で求められることが分かる。
  # -(x_0 + x_N-1)%3
  # なので、1 + pow(3, k) <= N になる最小の非負整数 k を使って 1 + pow(3, k) 段のピラミッドの頂点を求め、
  # その頂点を横に並べて新しいピラミッドを構築する、というのを繰り返すことで高速に答えを求めることができる。
  i_to_c = ["B", "W", "R"]
  N = int(input())
  C = [i_to_c.index(x) for x in list(input())]

  while len(C) > 1:
    N = len(C)
    temp = []
    mag = 1
    while 1+mag*3 < N:
      mag*=3
    for i in range(N-mag):
      temp.append((-(C[i]+C[i+mag]))%3)
    C = temp
  print(i_to_c[C[0]])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()