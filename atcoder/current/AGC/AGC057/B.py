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
        input = """4 2
5 8 12 20"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 5
24 25 26 27"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 1
24 25 26 27"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10 5
3 6 7 16 16 19 23 33 39 40"""
        output = """13"""
        self.assertIO(input, output)

def resolve():
  # A[i]//2 - X ~ A[i]//2 に関してはまとめて取り扱っても良い。(最終的に同値にできるので)
  # 例 4 を見る。23 と 33 が最終的に遠くなる。
  # もしも同値にできるのであれば、それは 30 回の操作以内に収まるはず。
  # 
  inf = 10**18+1
  N, X = map(int, input().split(" "))
  A = sorted([int(x) for x in input().split(" ")])
  ans = inf
    

  print(*A)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()