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
2100 2500 2700 2700"""
        output = """2 2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
1100 1900 2800 3200 3200"""
        output = """3 5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """20
800 810 820 830 840 850 860 870 880 890 900 910 920 930 940 950 960 970 980 990"""
        output = """1 1"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  N = int(input())
  A = [int(x) for x in input().split(" ")]
  agg = defaultdict(int)
  for i in range(N):
    agg[min(A[i]//400, 8)]+=1
  
  ans_min = 0
  for key, val in agg.items():
    if key < 8: ans_min+=1
  print(max(1, ans_min), ans_min+agg[8])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()