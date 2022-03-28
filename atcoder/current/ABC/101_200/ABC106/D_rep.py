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
        input = """2 3 1
1 1
1 2
2 2
1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 3 2
1 5
2 8
7 10
1 7
3 10"""
        output = """1
1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 10 10
1 6
2 9
4 5
4 7
4 7
5 8
6 6
6 7
7 9
10 10
1 8
1 9
1 10
2 8
2 9
2 10
3 8
3 9
3 10
1 10"""
        output = """7
9
10
6
8
9
6
7
8
10"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, M, Q = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(M)]

  integral = [[0]*(N+1) for _ in range(N+1)]
  for l, r in A:
    integral[l][r] += 1

  for i in range(1, N+1):
    for j in range(1, N+1):
      integral[i][j] += integral[i-1][j] + integral[i][j-1] - integral[i-1][j-1]

  for _ in range(Q):
    l, r = [int(x) for x in input().split(" ")]
    l -= 1
    ans = integral[r][r] + integral[l][l] - integral[r][l] - integral[l][r]
    print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()