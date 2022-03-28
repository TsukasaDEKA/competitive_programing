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
        input = """30 500 20 103"""
        output = """0.042553191489"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """50 500 100 1"""
        output = """1.000000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 2 1 1000"""
        output = """0.000000000000"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  A, B, C, X = map(int, input().split(" "))
  if X <= A:
    print(1.0)
    return
  if X > B:
    print(0.0)
    return

  print(C/(B-A))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()