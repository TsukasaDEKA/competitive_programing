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
2 3
1 1
3 2"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
1 1
1 1
1 5
1 100"""
        output = """101"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
3 10
48 17
31 199
231 23
3 2"""
        output = """6930"""
        self.assertIO(input, output)

def resolve():
  # 現在の得票数が t, a だとすると
  # t <= k*Ti かつ a <= k*Ai となる最小の k を求めれば良い。
  N = int(input())

  # 初期値
  t, a = [int(x) for x in input().split(" ")]
  for _ in range(N-1):
    T, A = [int(x) for x in input().split(" ")]
    k_t, k_a = (t+T-1)//T, (a+A-1)//A
    k = max(k_t, k_a)
    t, a = k*T, k*A

  print(t+a)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()