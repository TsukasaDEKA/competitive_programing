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
        input = """5 3
1 2 2 4 5"""
        output = """7.000000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 1
6 6 6 6"""
        output = """3.500000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 4
17 13 13 12 15 20 10 13 17 11"""
        output = """32.000000000000"""
        self.assertIO(input, output)

def resolve():
  from itertools import accumulate # 累積和作るやつ

  N, K = map(int, input().split(" "))
  P = list(accumulate([0.0]+[((y+1)*y//2)/y for y in [int(x) for x in input().split(" ")]]))

  ans = 0
  for i in range(K, N+1):
    ans = max(ans, P[i]-P[i-K])

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()