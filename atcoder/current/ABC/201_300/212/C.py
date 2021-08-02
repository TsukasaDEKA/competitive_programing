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
        input = """2 2
1 6
4 9"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1
10
10"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6 8
82 76 82 82 71 70
17 39 67 2 45 35 22 24"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  from bisect import bisect_left
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  B = sorted([int(x) for x in input().split(" ")])

  ans = inf
  for i in range(N):
    b1 = bisect_left(B, A[i])-1
    b2 = min(M-1, max(0, b1-1))
    # print(b1, b2)
    ans = min(ans, abs(A[i]-B[b1]), abs(A[i]-B[b2]))

  print(ans)
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()