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
        input = """0011"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """11011010001011"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  S = [int(x) for x in list(input())]
  N = len(S)
  count = [0, 0]
  for i in range(N):
    count[S[i]]+=1

  print(2*min(count[0], count[1]))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()