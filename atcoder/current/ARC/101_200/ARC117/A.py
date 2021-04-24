import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """1 1"""
        output = """1001 -1001"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 4"""
        output = """-8 -6 -9 120 -97"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7 5"""
        output = """323 -320 411 206 -259 298 -177 -564 167 392 -628 151"""
        self.assertIO(input, output)


def resolve():
  inf = 10**18+1
  A, B = map(int, input().split(" "))

  EA = [i+1 for i in range(A)]
  EB = [-i-1 for i in range(B)]
  if A > B:
    EB[-1] -= sum(EA[B:])
  elif A < B:
    EA[-1] -= sum(EB[A:])
  print(*EA, *EB, sep=" ")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
