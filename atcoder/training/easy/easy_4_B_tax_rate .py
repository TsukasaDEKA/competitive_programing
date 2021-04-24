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
        input = """432"""
        output = """400"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1079"""
        output = """:("""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1001"""
        output = """927"""
        self.assertIO(input, output)

from math import ceil, floor

def resolve():
  N = int(input())
  tax = 0.08

  if floor(ceil(N/(1+tax))*(1+tax)) == N:
    print(ceil(N/(1+tax)))
  else:
    print(":(")

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
    unittest.main()
