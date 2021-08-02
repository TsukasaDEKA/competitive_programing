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
        input = """7392"""
        output = """16 5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """12345"""
        output = """6 9"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """917237645269816381478124891628461341894621418946786785634501961"""
        output = """142 163"""
        self.assertIO(input, output)

def resolve():
  S = [int(x) for x in list(input())][::-1]
  even = 0
  odd = 0
  for i in range(len(S)):
    if i % 2: odd += S[i]
    else: even += S[i]
  print(odd, even, sep=" ")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()