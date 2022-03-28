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
        input = """3
abc
cde"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
a
z"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
expr
expr"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  S = list(input())
  T = list(input())

  for i in range(N+1):
    s = S[:i]+T
    if s[:N] == S and s[i:] == T:
      print(len(s))
      return

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()