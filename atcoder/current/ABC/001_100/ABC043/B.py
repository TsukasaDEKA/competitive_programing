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
        input = """01B0"""
        output = """00"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """0BB1"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  S = list(input())
  ans = []
  for s in S:
    if s != "B":
      ans.append(s)
    elif ans:
      ans.pop()

  print("".join(ans))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()