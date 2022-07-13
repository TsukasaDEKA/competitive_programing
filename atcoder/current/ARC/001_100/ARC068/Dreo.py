from itertools import count
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
        input = """5
1 2 1 3 7"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """15
1 3 5 2 1 3 2 8 8 6 2 6 11 1 1"""
        output = """7"""
        self.assertIO(input, output)

def resolve():
  from collections import Counter, defaultdict
  # 大きい方から処理していけば良い？
  N = int(input())
  A = sorted([int(x) for x in input().split(" ")])
  counts = Counter(A)
  agg = [[] for _ in range(2)]
  for key, value in counts.items():
    agg[value%2].append(key)

  ans = len(agg[1]) + len(agg[0])
  if len(agg[0])%2:
    ans -= 1
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()