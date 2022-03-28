import sys
from io import StringIO
from traceback import print_tb
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
        input = """7 0 6 30"""
        output = """Aoki"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7 30 7 30"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """0 0 23 59"""
        output = """Takahashi"""
        self.assertIO(input, output)

def resolve():
  A, B, C, D = map(int, input().split(" "))
  if A < C:
    print("Takahashi")
    return
  if A > C:
    print("Aoki")
    return
  
  if B <= D:
    print("Takahashi")
  else:
    print("Aoki")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()