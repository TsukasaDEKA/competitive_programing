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
        input = """5 4
9 8 3 7 2
1 6 2 9 5"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 90
1 1 1 100
1 2 3 100"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 1000000000
1 1 1000000000 1000000000
1 1000000000 1 1000000000"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]
  X_A = [0]*N
  X_B = [0]*N
  X_A[0] = A[0]
  X_B[0] = B[0]
  for i in range(1, N):
    if abs(X_A[i-1]-A[i]) <= K or abs(X_B[i-1]-A[i]) <= K:
      X_A[i] = A[i]
    else:
      X_A[i] = inf

    if abs(X_A[i-1]-B[i]) <= K or abs(X_B[i-1]-B[i]) <= K:
      X_B[i] = B[i]
    else:
      X_B[i] = inf
    if X_A[i] == inf and X_B[i] == inf:
      print("No")
      return

  print("Yes")


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()