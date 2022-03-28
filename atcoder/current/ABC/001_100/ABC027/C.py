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
        output = """Aoki"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7"""
        output = """Aoki"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """123456789123456789"""
        output = """Aoki"""
        self.assertIO(input, output)

def resolve():
  # DP っぽい
  # 一回の操作でパターン数は 2 倍に増える。
  # N <= 10**18 なので最大 60 回程度の操作しかしない。
  # i の時に手番をとったら負けるゾーンがある。
  # => 遷移先に i を選べる場合はそこに放り込めば勝ち。
  # => i に遷移できるならば勝ち
  # 遷移を考えるのが厄介。
  
  N = int(input())+1
  win = False
  while N > 1:
    win = not win
    N = (N+1)//2 if win else (N)//2

  print("Takahashi" if not win else "Aoki")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()