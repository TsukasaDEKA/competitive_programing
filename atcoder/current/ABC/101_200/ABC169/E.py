import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """2
1 2
2 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
100 100
10 10000
1 1000000000"""
        output = """9991"""
        self.assertIO(input, output)

def resolve():
  # A, B は独立で考えられる。
  N = int(input())
  A = [0]*N
  B = [0]*N
  for i in range(N):
    a, b = map(int, input().split(" "))
    A[i] = a
    B[i] = b
  A.sort()
  B.sort(reverse=True)
  center = (N-1)//2
  if N%2:
    l = A[center]
    r = B[center]
  else:
    l = sum(A[center:center+2])
    r = sum(B[center:center+2])
  ans = r-l+1
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
