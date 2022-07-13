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
        input = """5 4 7
8 3 10 5 13"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 100 7
8 3 10 5 13"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """20 815 60
2066 3193 2325 4030 3725 1669 1969 763 1653 159 5311 5341 4671 2374 4513 285 810 742 2981 202"""
        output = """112"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, K, X = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  for i in range(N):
    if A[i] >= X:
      k = min(A[i]//X, K)
      K -= k
      A[i]-= X*k


  A.sort(reverse=True)
  for i in range(N):
    if K == 0: break
    A[i] = 0
    K -= 1

  print(sum(A))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()