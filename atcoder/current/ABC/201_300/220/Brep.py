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
  A, B = [[int(p) for p in list(x)] for x in input().split(" ")]
  a = 0
  for i in range(len(A)):
    a+=A[i]*pow(K, len(A)-i-1)

  b = 0
  for i in range(len(B)):
    b+=B[i]*pow(K, len(B)-i-1)

  print(a*b)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()