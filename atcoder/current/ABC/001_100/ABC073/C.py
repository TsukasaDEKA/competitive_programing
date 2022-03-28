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
        input = """3
6
2
6"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
2
5
5
2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
12
22
16
22
18
12"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  N = int(input())
  A = [int(input()) for _ in range(N)]
  agg = defaultdict(int)
  for a in A:
    agg[a] += 1
  
  print(len([v for v in agg.values() if v%2]))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()