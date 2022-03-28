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
32.2 25.3
36.4 26.4
24.1 18.0
26.0 24.9"""
        output = """1 1 1 2 0 0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
-2 -5.2
2 -0.1
26.0 -0.1"""
        output = """0 0 1 0 2 1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
15.0 9.5
12.5 10.5
20.5 19.9
15.5 15.5"""
        output = """0 0 0 0 0 0"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  agg = [0]*6
  for _ in range(N):
    max_, min_ = [float(x) for x in input().split(" ")]

    if max_ >= 35: agg[0]+=1
    elif max_ >= 30: agg[1]+=1
    elif max_ >= 25: agg[2]+=1

    if min_ >= 25: agg[3]+=1
    elif min_ < 0 and max_ >= 0: agg[4]+=1
    elif max_ < 0: agg[5]+=1

  print(*agg)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()