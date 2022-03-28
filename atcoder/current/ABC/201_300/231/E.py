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
        input = """3 87
1 10 100"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 49
1 7"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 123456789012345678
1 100 10000 1000000 100000000 10000000000 1000000000000 100000000000000 10000000000000000 1000000000000000000"""
        output = """233"""
        self.assertIO(input, output)

def resolve():
  from bisect import bisect_left

  # N はとても少ない。
  # 全探索？

  inf = 10**18+1
  N, X = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  # N が 1 の時は自明
  if N == 1:
    print(X)
    return
  
  # N が 2 以上の時について考える。
  # A[1] を基準 a と考える。
  a = A[1]

  # X が a の倍数の時、A[0] を使わないのが良い。
  if X%a == 0:
    
    return
  
  q = X%a

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()