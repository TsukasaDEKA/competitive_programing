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
        input = """2"""
        output = """1 2 1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4"""
        output = """1 2 1 3 1 2 1 4 1 2 1 3 1 2 1"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """16"""
        output = """1 2 1 3 1 2 1 4 1 2 1 3 1 2 1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())

  def S(n):
    if n == 1:
      return [1]
    else:
      return [*S(n-1), n, *S(n-1)]

  print(*S(N), sep=" ")


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()