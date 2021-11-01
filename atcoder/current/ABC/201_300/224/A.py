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
        input = """atcoder"""
        output = """er"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """tourist"""
        output = """ist"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """er"""
        output = """er"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  S = input()

  if S[-2:] == "er":
    print("er")
  else:
    print("ist")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()