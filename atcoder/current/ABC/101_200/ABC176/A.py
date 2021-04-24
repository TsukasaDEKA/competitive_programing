import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """20 12 6"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000 1 1000"""
        output = """1000000"""
        self.assertIO(input, output)

from math import ceil
def resolve():
  N, X, T = map(int, input().split(" "))

  if N > X:
    print(ceil(N/X)*T)
  else:
    print(T)
if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()