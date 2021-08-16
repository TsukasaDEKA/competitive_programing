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
        input = """4 5 2
3 2
2 5"""
        output = """2 1
1 2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000000000 1000000000 10
1 1
10 10
100 100
1000 1000
10000 10000
100000 100000
1000000 1000000
10000000 10000000
100000000 100000000
1000000000 1000000000"""
        output = """1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9
10 10"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  H, W, N= map(int, input().split(" "))
  A = []
  B = []
  for i in range(N):
    a, b = map(int, input().split(" "))
    A.append((a, i))
    B.append((b, i))
  A.sort()
  B.sort()
  ans = [[0]*2 for _ in range(N)]

  A_count = set()
  B_count = set()
  for i in range(N):
    av, aj = A[i]
    bv, bj = B[i]
    A_count.add(av)
    B_count.add(bv)
    ans[aj][0] = len(A_count)
    ans[bj][1] = len(B_count)

  for a, b in ans:
    print(a, b)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()