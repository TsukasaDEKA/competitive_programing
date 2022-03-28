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
  N = int(input())
  T, A = 1, 1
  for i in range(N):
    t, a = [int(x) for x in input().split(" ")]
    # 前回の得票数以上かつ最小の t, a の倍数
    T = ((T+t-1)//t)*t
    A = ((A+a-1)//a)*a
    g = max(T//t, A//a)
    T = g*t
    A = g*a
  print(T+A)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()