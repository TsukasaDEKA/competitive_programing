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
        input = """3
3 5 2
26"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
12 34 56 78
1000"""
        output = """23"""
        self.assertIO(input, output)


def resolve():
  from bisect import bisect_left
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  X = int(input())

  sumA = [0]*(N)
  sumA[0] = A[0]
  for i in range(1, N):
    sumA[i] = sumA[i-1]+A[i]

  k = (X//sumA[-1])*N
  X %= sumA[-1]
  for i in range(N):
    if X < 0:
      print(k)
      return
    k+=1
    X-=A[i]
  print(k)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()