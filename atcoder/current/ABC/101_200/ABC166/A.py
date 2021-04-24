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
        input = """ABC"""
        output = """ARC"""
        self.assertIO(input, output)

from math import gcd
from functools import reduce
from itertools import product

def resolve():
  contest = input()

  print("ARC" if contest == "ABC" else "ABC")


if __name__ == "__main__":
    resolve()

if __name__ == "__main__":
    unittest.main()