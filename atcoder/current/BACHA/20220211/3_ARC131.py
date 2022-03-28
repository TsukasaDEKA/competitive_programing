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
        input = """6
9 14 11 3 5 8"""
        output = """Lose"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
131"""
        output = """Win"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8
12 23 34 45 56 78 89 98"""
        output = """Win"""
        self.assertIO(input, output)

def resolve():
  # 初手で 0 にできるなら勝てるのは自明。
  # 2 手で 0 にできるのであれば相手の勝ち。
  # 2 手で 0 にできるペアがあるとする。
  # 片方を先に選んだ方が負け。
  # 偶数かつ、1 手でゲームが終わらない場合を考える。
  # 相手の手番では奇数。
  # 全てのコマが「他のコマを引けば終わる」ペアに属しているという状況はありえない。(奇数なので)
  # なので相手は「他のコマを引けば終わる」ペアに属していないコマを取ることができる。
  # 最後までその状態を維持できるので相手の勝ち。

  N = int(input())
  A = [int(x) for x in input().split(" ")]
  xorA = 0
  for a in A: xorA ^= a

  for a in A:
    if xorA^a == 0:
      print("Win")
      return

  print("Win" if N%2 else "Lose")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()