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
        input = """41 2
5 6"""
        output = """30"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """10 2
5 6"""
        output = """-1"""
        self.assertIO(input, output)
    def test_Sample_Input_3(self):
        input = """11 2
5 6"""
        output = """0"""
        self.assertIO(input, output)
    def test_Sample_Input_4(self):
        input = """314 15
9 26 5 35 8 9 79 3 23 8 46 2 6 43 3"""
        output = """9"""
        self.assertIO(input, output)

from math import gcd
from functools import reduce
from itertools import product

def resolve():
  K, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  print(K-sum(A) if K-sum(A) >= 0 else -1)

# if __name__ == "__main__":
#     resolve()

if __name__ == "__main__":
    unittest.main()