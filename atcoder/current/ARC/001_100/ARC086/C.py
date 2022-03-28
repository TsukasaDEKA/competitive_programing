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
        input = """5 2
1 1 2 2 5"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 4
1 1 2 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 3
5 1 3 2 4 1 1 2 3 4"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  # 集計とって少ない順から消していく。
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  agg = defaultdict(int)
  for a in A:
    agg[a]+=1

  agg = sorted(list(agg.items()), key=lambda x: x[1])
  N = len(agg)
  ans = 0
  for i in range(N-K):
    ans+=agg[i][1]
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()