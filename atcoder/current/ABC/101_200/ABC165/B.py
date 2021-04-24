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
        input = """103"""
        output = """3"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """1000000000000000000"""
        output = """3760"""
        self.assertIO(input, output)
    def test_Sample_Input_3(self):
        input = """1333333333"""
        output = """1706"""
        self.assertIO(input, output)


from math import gcd
from functools import reduce
from itertools import product

def resolve():
  X = int(input())

  years = 0
  money = 100
  while money < X:
    money = int(money * 1.01)
    years += 1
  print(years)

if __name__ == "__main__":
    resolve()

if __name__ == "__main__":
    unittest.main()