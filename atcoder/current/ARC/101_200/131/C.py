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
  # 解説 AC。
  # N が奇数であれば先手必勝。
  ## 証明
  # V を A の全部の要素を xor した値だとすると、
  # 先手が任意の Ai を選び、後手が Aj を選んだ時に勝利するのであれば、
  # V^Ai^Aj = 0 となる。
  # つまり V = Ai^Aj
  # Ai != Aj (i != j) である点に注意する。
  # その場合、V = Ai^Aj となる Aj の組み合わせは各 Ai に対して必ず一つ存在しなければならない。
  # 選ばれた Ai に対して V = Ai^Aj となる Aj が存在しない場合、
  # 先手はそれを選ぶことで次の手で後手が勝利することを防ぐことができるためである。
  # しかし、奇数の場合、Ai と Aj のペアを順に作っていくと、最終的に 1 つ余る事になる。
  # なので、上記の事が成り立たず、後手が勝つ事ができる状況にはならない。
  # なので先手必勝となる。
  # 
  from bisect import bisect_left

  inf = 10**18+1
  N = int(input())
  A = sorted([int(x) for x in input().split(" ")])
  if N%2:
    print("Win")
    return

  V = 0
  for i in range(N):
    V ^= A[i]

  for i in range(N):
    if V^A[i] == 0:
      print("Win")
      return
  print("Lose")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()