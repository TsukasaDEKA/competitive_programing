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
        input = """7
500 600"""
        output = """OK"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """4
5 7"""
        output = """NG"""
        self.assertIO(input, output)
    def test_Sample_Input_3(self):
        input = """1
11 11"""
        output = """OK"""
        self.assertIO(input, output)


from math import gcd
from functools import reduce
from itertools import product

def resolve():
  K = int(input())
  A, B = map(int, input().split(" "))

  result = False
  for i in range(A, B+1):
    if i%K == 0:
      result = True
      break
  print("OK" if result else "NG")
# if __name__ == "__main__":
#     resolve()


if __name__ == "__main__":
    unittest.main()