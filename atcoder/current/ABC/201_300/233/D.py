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
        input = """6 5
8 -3 5 7 0 -4"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 -1000000000000000
1000000000 -1000000000"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  from itertools import accumulate # 累積和作るやつ
  from collections import defaultdict

  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  accA = [0] + list(accumulate(A))
  agg = defaultdict(int)
  ans = 0
  for i in range(N+1):
    ans+=agg[accA[i]-K]
    agg[accA[i]]+=1

  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()