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
        input = """2 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 100"""
        output = """91"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 2"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  A, B = map(int, input().split(" "))

  print(B-A+1 if B-A+1 > 0 else 0)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()