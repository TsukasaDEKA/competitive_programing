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
        input = """1 4 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7 7 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """31 415926 5"""
        output = """6"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  A, B, K = map(int, input().split(" "))

  for i in range(1000):
    if A >= B:
      print(i)
      return
    A*=K

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()