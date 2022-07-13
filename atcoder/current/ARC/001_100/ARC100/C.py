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
        input = """5
2 2 3 5 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """9
1 2 3 4 5 6 7 8 9"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
6 5 4 3 2 1"""
        output = """18"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """7
1 1 1 1 2 3 4"""
        output = """6"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # 先に Ai - i をやっておくと良さげ？
  # 答えで二分探索・・・？ => 線形性はあるのか？
  N = int(input())
  A = sorted([int(x)-i for i, x in enumerate(input().split(" "))])
  # 中央値 を b にしてみる。
  b = A[N//2] if N%2 else (A[N//2]+A[N//2-1])//2
  ans = sum([abs(x-b) for x in A])
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()