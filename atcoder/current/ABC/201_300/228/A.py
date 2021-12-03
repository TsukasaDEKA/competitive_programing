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
        input = """7 20 12"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """20 7 12"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """23 0 23"""
        output = """Yes"""
        self.assertIO(input, output)


def resolve():
  S, T, X = map(int, input().split(" "))

  if T < S: T += 24
  if X < S: X += 24
  print("Yes" if S <= X and X < T else "No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()