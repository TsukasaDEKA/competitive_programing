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
        input = """chokudai
chokudaiz"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """snuke
snekee"""
        output = """No"""
        self.assertIO(input, output)
    def test_Sample_Input_3(self):
        input = """a
aa"""
        output = """Yes"""
        self.assertIO(input, output)


from math import gcd
from functools import reduce
from itertools import product

def resolve():
  S = input()
  T = input()

  print("Yes" if T[:-1]==S else "No")

if __name__ == "__main__":
    resolve()

if __name__ == "__main__":
    unittest.main()