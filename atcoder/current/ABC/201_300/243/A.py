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
        input = """25 10 11 12"""
        output = """T"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """30 10 10 10"""
        output = """F"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100000 1 1 1"""
        output = """M"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  V, A, B, C = map(int, input().split(" "))

  i = 0
  member = ["F", "M", "T"]
  val = [A, B, C]
  while V >= 0:
    if V >= val[i]:
      V -= val[i]
      i = (i+1)%3
    else:
      print(member[i])
      return

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()