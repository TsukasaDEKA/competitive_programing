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
2
4
3
1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
10
8
5
3
2"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  A = [int(input()) for _ in range(N)] 
  # ソートする時に偶数移動か奇数移動かを判定する。
  A = sorted([(x, i) for i, x in enumerate(A)])
  ans = 0
  for i in range(N):
    _, j = A[i]
    if abs(i-j)%2: ans+=1
  print((ans+1)//2)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()