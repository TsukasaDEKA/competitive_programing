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
        input = """2
1 2 3 5 7 11
4 6 8 9 10 12"""
        output = """1421"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
11 13 17 19 23 29"""
        output = """112"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
19 23 51 59 91 99
15 45 56 65 69 94
7 11 16 34 59 95
27 30 40 43 83 85
19 23 25 27 45 99
27 48 52 53 60 81
21 36 49 72 82 84"""
        output = """670838273"""
        self.assertIO(input, output)

def resolve():
  mod = 10**9+7
  N = int(input())
  ans = sum([int(x) for x in input().split(" ")])
  for i in range(N-1):
    ans *= sum([int(x) for x in input().split(" ")])
    if ans >= mod: ans%=mod

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()