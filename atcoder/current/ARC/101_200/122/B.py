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

    def test_入力例_1(self):
        input = """3
3 1 4"""
        output = """1.83333333333333333333"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
866111664 178537096 844917655 218662351 383133839 231371336 353498483 865935868 472381277 579910117"""
        output = """362925658.10000000000000000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
10"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2
10 10"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # 中央値の半額？差の合計の半額？
  N = int(input())
  A = sorted([int(x) for x in input().split(" ")])
  sum_A = sum(A)
  ans = 0
  x = 0
  if N%2: x = A[N//2]
  else: x = (A[N//2]+A[N//2])/2

  x/=2
  for i in range(N):
    ans += x + A[i] - min(A[i], 2*x)
  print(ans/N)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
