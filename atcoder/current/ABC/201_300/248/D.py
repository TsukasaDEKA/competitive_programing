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
3 1 4 1 5
4
1 5 1
2 4 3
1 5 2
1 3 3"""
        output = """2
0
0
1"""
        self.assertIO(input, output)



def resolve():
  # input = sys.stdin.readline()
  from bisect import bisect_left, bisect_right

  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  print(N, file=sys.stderr)
  print(A, file=sys.stderr)
  aggA = [[] for _ in range(N+1)]
  for i in range(N):
    aggA[A[i]].append(i)

  Q = int(input())
  for q in range(Q):
    l, r, x = [int(x) for x in input().split(" ")]
    l, r = l-1, r-1
    agg = aggA[x]
    left_i = bisect_left(agg, l)
    right_i = bisect_right(agg, r)
    print(max(0, right_i - left_i))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()