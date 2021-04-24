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
        input = """2"""
        output = """9"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """200"""
        output = """10813692"""
        self.assertIO(input, output)

from math import gcd
from functools import reduce
from itertools import product

def resolve():
  K = int(input())
  # result = sum([ gcd(gcd(x[0], x[1]), x[2]) for x in itertools.product(range(1, K+1), range(1, K+1), range(1, K+1)) ])
  step1 = [ gcd(x[0], x[1]) for x in product(range(1, K+1), range(1, K+1)) ]
  result = sum([ gcd(x[0], x[1]) for x in product(step1, range(1, K+1)) ])
  print(result)

  # gcds = []
  # for a in range(1, K+1):
  #   for b in range(1, K+1):
  #     for c in range(1, K+1):
  #       gcds.append(gcd_list([a, b, c]))

  # print(sum(gcds))

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
  unittest.main()