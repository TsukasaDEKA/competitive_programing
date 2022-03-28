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
1 1 3
3 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1
1000000000
1"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 2
1 2 3 4 5
5 5"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  inf = 10**18+1
  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]
  agg = defaultdict(int)
  for a in A:
    agg[a]+=1
  for b in B:
    if agg[b] == 0:
      print("No")
      return
    agg[b] -= 1
  print("Yes")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()