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
        input = """4
4 8 12 90"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """20
313923 246114 271842 371982 284858 10674 532090 593483 185123 364245 665161 241644 604914 645577 410849 387586 732231 952593 249651 36908"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
1 1 1 1 1"""
        output = """10"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = sorted([int(x) for x in input().split(" ")])
  # 0 桁目が 9-A[i][0] 以下かつ 1 桁目が 9-A[i][1] 以下かつ・・・な組み合わせを見つける問題。
  # 集合が桁数分存在することになって比較が大変。
  # 最初に集計をとる。
  # 1 桁目が x 以下かつ 2 桁目が ~~ 以下かつ・・・
  # 10 パターン * 6 なので普通にやったら 10**5 * (10**6) 回の計算
  # DP 的にできないか？
  # 

  print(A)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()