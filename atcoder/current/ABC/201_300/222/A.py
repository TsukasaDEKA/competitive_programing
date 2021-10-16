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
        input = """321"""
        output = """0321"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7777"""
        output = """7777"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1"""
        output = """0001"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = input()

  print(N.zfill(4))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()