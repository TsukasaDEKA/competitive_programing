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
        input = """023456789"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """459230781"""
        output = """6"""
        self.assertIO(input, output)

def resolve():
  input = sys.stdin.readline().rstrip
  inf = 10**18+1
  print(45-sum(map(int, list(input()))))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()