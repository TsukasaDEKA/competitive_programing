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
        input = """198 1.10"""
        output = """217"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 0.00"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1000000000000000 9.99"""
        output = """9990000000000000"""
        self.assertIO(input, output)

import numpy as np
import math
from decimal import Decimal

def resolve():
  A, B = map(str, input().split(" "))
  
  # print(math.floor(int(S[0])*Decimal(S[1])))
  # print(math.floor((int(S[0]) * int(float(S[1])*100))) // 100)
  print(math.floor((int(A) * int(float(B)*100))) // 100)
# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
    unittest.main()
