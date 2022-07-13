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

    def test_入力例_1(self):
        input = """2 3
2
1 2
2
2 3
1 0 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3
1
1
1
2
0 1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 2
1
1
1
2
1
2
1 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """13 6
3
1 3 5
3
1 4 5
4
3 4 5 6
2
2 5
4
1 2 3 5
3
3 4 6
3
4 5 6
6
1 2 3 4 5 6
4
1 3 5 6
3
1 2 4
3
1 5 6
4
1 2 3 4
1
5
1 0 0 1 0 0"""
        output = """128"""
        self.assertIO(input, output)


def resolve():
  # 押してはいけないボタンが存在する。
  # 例えば、S = 0 1 1 で、パネル 1 を操作するボタンが 1 個の時。
  # ボタン同士の XOR をとるとそれらを全部押した時の結果が見える。
  # 例えば 1 1 1 のボタンと 0 1 1 のボタンを押した時、結果は 1 0 0 になる。
  # 2**300 は間に合わない。
  # 入力例 4 がなぜ 128 なのかを考えるとどうにかなるかも。128 = 2**7
  # 例は全て 2 の乗数。
  # 入力例 4 のデータを並び替えてみると面白い。
  # - [0, 0, 0, 0, 1, 0]
  # - [0, 0, 0, 1, 1, 1]
  # - [0, 0, 1, 1, 0, 1]
  # - [0, 0, 1, 1, 1, 1]
  # - [0, 1, 0, 0, 1, 0]
  # - [1, 0, 0, 0, 1, 1]
  # - [1, 0, 0, 1, 1, 0]
  # - [1, 0, 1, 0, 1, 0]
  # - [1, 0, 1, 0, 1, 1]
  # - [1, 1, 0, 1, 0, 0]
  # - [1, 1, 1, 0, 1, 0]
  # - [1, 1, 1, 1, 0, 0]
  # - [1, 1, 1, 1, 1, 1]
  # ここで、行はスイッチ、列はパネルである。
  # パネル 1 に着目した場合、
  # 1 ~ 5 番目のスイッチは結果に影響がなくて、
  # 6 ~ 13番目のスイッチの中から奇数個選ぶことで
  # パネル 1 を最終的に 1 にすることができる。
  # 全部選ぶのは辛そう。
  # 5 番目のパネルを ON OFF するボタンは独立しているので、
  # 他のボタンを押した時の結果に合わせて押すことで、最終的に S にフィットさせることができる。
  # 実は 049 の発展系では？
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  A_M = [0]*N
  for n in range(N):
    _ = input()
    A = [int(x)-1 for x in input().split(" ")]
    for a in A:
      A_M[n] += 1<<a
  A_M.sort(reverse=True)
  # 三角行列を作る。
  for i in range(min(N, M)):
    if (A_M[i]>>i)&1:
      pass
  print(*sorted(A_M), sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
