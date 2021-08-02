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
1 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
3 3 4 4"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2
1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10
999999917 999999914 999999923 999999985 999999907 999999965 999999914 999999908 999999951 999999979"""
        output = """405924645"""
        self.assertIO(input, output)

def resolve():
  mod = 10**9+7
  N = int(input())
  C = sorted([int(x) for x in input().split(" ")])

  ans = 1
  for i in range(N):
    ans *= (C[i]-i)
    if ans>=mod: ans %= mod

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()