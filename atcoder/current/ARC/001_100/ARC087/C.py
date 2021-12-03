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
        input = """4
3 3 3 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
2 4 1 4 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
1 2 2 3 3 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1
1000000000"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """8
2 7 1 8 2 8 1 8"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  agg = defaultdict(int)
  for a in A:
    agg[a]+=1
  ans = 0
  for k, v in agg.items():
    ans+=max(0, v-k, v%k)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()