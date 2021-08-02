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
        input = """8 3 2"""
        output = """2.000000000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """8 5 2"""
        output = """1.600000000000000"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  A, B, C = map(int, input().split(" "))

  temp = A
  for i in range(temp):
    if A > B*C: A-=1
    else:
      print(A/B)
      return

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()