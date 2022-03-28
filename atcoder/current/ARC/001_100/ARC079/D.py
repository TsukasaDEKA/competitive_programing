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
        input = """0"""
        output = """4
3 3 3 3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1"""
        output = """3
1 0 3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2"""
        output = """2
2 2"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """3"""
        output = """7
27 0 0 0 0 0 0"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """1234567894848"""
        output = """10
1000 193 256 777 0 1 1192 1234567891011 48 425"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  K = int(input())

  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()