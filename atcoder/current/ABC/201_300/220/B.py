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
        input = """2
1011 10100"""
        output = """220"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7
123 456"""
        output = """15642"""
        self.assertIO(input, output)

def resolve():
  K = int(input())
  A, B = [int(x, K) for x in input().split(" ")]
  print(A*B)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()