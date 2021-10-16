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
        input = """Hello,World!"""
        output = """AC"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """Hello,world!"""
        output = """WA"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """Hello!World!"""
        output = """WA"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = input()

  print("AC" if N == "Hello,World!" else "WA")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()