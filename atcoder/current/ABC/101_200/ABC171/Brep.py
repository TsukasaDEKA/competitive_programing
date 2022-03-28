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
50 100 80 120 80"""
        output = """210"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1
1000"""
        output = """1000"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, K = map(int, input().split(" "))
  A = sorted([int(x) for x in input().split(" ")])

  print(sum(A[:K]))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()