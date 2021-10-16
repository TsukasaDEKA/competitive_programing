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
        input = """56"""
        output = """14"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """32"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """0"""
        output = """40"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """100"""
        output = """expert"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  X = int(input())

  if X < 40:
    print(40-X)
  elif X < 70:
    print(70-X)
  elif X < 90:
    print(90-X)
  else:
    print("expert")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()