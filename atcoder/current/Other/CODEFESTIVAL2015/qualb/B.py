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
2 1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 2
2 1 2 1"""
        output = """?"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 1
0 0 0 0 0 0 1 1 1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10 5
0 1 2 3 4 5 5 5 5 5"""
        output = """?"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  inf = 10**18+1
  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  agg = defaultdict(int)
  for a in A:
    agg[a]+=1
    if agg[a] > N//2:
      print(a)
      return
  print("?")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()