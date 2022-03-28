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
        input = """3x7"""
        output = """21"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """9x9"""
        output = """81"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1x1"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  a, x, b = list(input())

  print(int(a)*int(b))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()