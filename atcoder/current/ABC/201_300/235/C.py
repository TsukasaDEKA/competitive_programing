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
        input = """6 8
1 1 2 3 1 2
1 1
1 2
1 3
1 4
2 1
2 2
2 3
4 1"""
        output = """1
2
5
-1
3
6
-1
-1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 2
0 1000000000 999999999
1000000000 1
123456789 1"""
        output = """2
-1"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  inf = 10**18+1
  N, Q = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  agg = defaultdict(list)
  for i in range(N):
    agg[A[i]].append(i)

  for _ in range(Q):
    x, k = [int(x) for x in input().split(" ")]
    if len(agg[x]) < k:
      print(-1)
      continue
    print(agg[x][k-1]+1)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()