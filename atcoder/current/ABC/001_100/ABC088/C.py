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
        input = """1 0 1
2 1 2
1 0 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2 2
2 1 2
2 2 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """0 8 8
0 8 8
0 8 8"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1 8 6
2 9 7
0 7 7"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  C = [[int(x) for x in input().split(" ")] for _ in range(3)]
  for i in range(3):
    c = min(C[i])
    for j in range(3):
      C[i][j] -= c

  print("Yes" if C[0] == C[1] and C[1] == C[2] else "No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()