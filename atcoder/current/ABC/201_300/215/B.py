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
        input = """6"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1000000000000000000"""
        output = """59"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  count = 0
  v = 1
  for i in range(70):
    if v > N:
      print(count-1)
      return
    v*=2
    count+=1

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()