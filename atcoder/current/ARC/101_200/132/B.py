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
1 3 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
2 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
2 3 4 5 6 7 8 9 10 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """12
1 2 3 4 5 6 7 8 9 10 11 12"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """4
4 3 2 1"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
  # 与えられる入力は操作によって順列を昇順に並び替えられることが保証されている。
  # 与えられた操作では P[i] の順序を変更することができないため、
  # P = P'[:i]+P'[i:] or reversed(P'[:i]+P'[i:]) のパターンのどちらかになる。
  # (P' は 1...N で i は 0 ~ N の任意の値)
  # 先頭を後方に移動 => 反転 => 先頭を後方に移動 => 反転 とすると元の数列に戻るため、
  # 基本的に操作を交互に繰り返す必要はない。
  # また、P が逆順の場合は反転回数は 1 回、そうでない場合は 0 or 2 回行う。
  N = int(input())
  P = [int(x)-1 for x in input().split(" ")]
  zero_i = P.index(0)
  # 全体的に反転しているかどうかを判定する。
  rev = P[(zero_i+1)%N] != 1

  if rev:
    # 前方から取っていって反転した場合と、反転して後方から取っていった場合の小さい方
    front_length = zero_i+1
    print(min(front_length+1, 1+N-front_length))
  else:
    # 前方から取っていった場合と、反転して後方から取っていった後に再度反転した場合の小さい方
    front_length = zero_i
    print(min(front_length, 1+N-front_length+1))
  # 整理すると以下のようにも書ける。
  # if rev: zero_i = N-zero_i
  # print(min(zero_i, N-zero_i+2))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()