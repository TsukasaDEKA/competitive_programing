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
        input = """6 2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7 4 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 1 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1000000000000000 1000000000000000 1000000000000000"""
        output = """1000000000000000"""
        self.assertIO(input, output)

def resolve():
  X, K, D = map(int, input().split(" "))
  X = abs(X)
  k = min(K, X//D)
  X -= k*D
  K -= k
  if K%2: X-=D
  print(abs(X))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()