from http.client import CONTINUE
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
        input = """3 2
URL"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 500000000000000000
RRUU"""
        output = """500000000000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """30 123456789
LRULURLURLULULRURRLRULRRRUURRU"""
        output = """126419752371"""
        self.assertIO(input, output)

def resolve():
  N, X = map(int, input().split(" "))
  S = input()

  ans = list(bin(X)[2:])
  for s in S:
    if s == "U":
      ans.pop()
    elif s == "L":
      ans.append("0")
    else:
      ans.append("1")

  print(int("".join(ans) , 2))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()