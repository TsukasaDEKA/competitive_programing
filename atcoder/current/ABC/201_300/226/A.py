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
        input = """3.456"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """99.500"""
        output = """100"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """0.000"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  N, P = map(int, input().split("."))
  if P//100 >= 5: N+=1
  print(N)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()