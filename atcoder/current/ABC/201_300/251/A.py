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
        input = """abc"""
        output = """abcabc"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """zz"""
        output = """zzzzzz"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  S = list(input())
  ans = []
  while len(ans) < 6:
    ans += S

  print("".join(ans))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()