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

    def test_Sample_Input_1(self):
        input = """3
3 9 6 4 6
6 9 3 1 1
8 8 9 3 7"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
6 13 6 19 11
4 4 12 11 18
20 7 19 2 5
15 5 12 20 7
8 7 6 18 5"""
        output = """13"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
6 7 5 18 2
3 8 1 6 3
7 2 8 7 7
6 3 3 4 7
12 8 9 15 9
9 8 6 1 10
12 9 7 8 2
10 3 17 4 10
3 1 3 19 3
3 14 7 13 1"""
        output = """10"""
        self.assertIO(input, output)

def resolve():
  # 最小値の最大化
  # 3000C3 = 4,495,501,000 なので全探索は無理。
  # 目標値二分探索で全要素を探ってみる。
  inf = 10**18+1
  N = int(input())
  ABI = sorted([[int(x) for x in input().split(" ")] for _ in range(N)])

  # 先にそれぞれの最大
  ans = 0
  for i in range(N):
    f = ABI[i]
    for j in range(N):
      s = ABI[j]
      s = min([max() for k in range(5)])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
