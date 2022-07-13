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
        input = """1 2
1 0
0 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2
1 2
3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2 1
90 80
70 60"""
        output = """70"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  R, C = [int(x)-1 for x in input().split(" ")]

  print([[int(x) for x in input().split(" ")] for _ in range(R+1)][R][C])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()