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
        input = """4 5
1 10 100 1000"""
        output = """101"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """20 1048575
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"""
        output = """210"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 0
1000 1000 1000 1000"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, X = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  ans = 0
  for j in range(N):
    if (X>>j)&1: ans+=A[j]

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()