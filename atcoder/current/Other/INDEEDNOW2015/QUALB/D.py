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
        input = """4 2
1 2 2 1"""
        output = """7
8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 4
1 4 2 3"""
        output = """4
6
4
6"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 1
1 1 1 1 1"""
        output = """15"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, C = map(int, input().split(" "))
  A = [int(x)-1 for x in input().split(" ")]
  agg = [[-1] for _ in range(C)]
  for i in range(N):
    agg[A[i]].append(i)

  for i in range(C):
    agg[i].append(N)

  all_pattern = (N*(N+1))//2
  ans = [all_pattern]*C
  for i in range(C):
    for j in range(len(agg[i])-1):
      length = agg[i][j+1]-agg[i][j]-1
      ans[i] -= (length*(length+1))//2
  print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()