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
        input = """4
0 1 3 2"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
4 3 2 1 0"""
        output = """31"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
40"""
        output = """1099511627776"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """8
2 0 2 2 0 4 2 4"""
        output = """80"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  T = [int(x) for x in input().split(" ")]
  A = [0]*N
  A[0] = 1<<T[0]

  for i in range(1, N):
    if A[i-1] < (1<<T[i]):
      A[i] = 1<<T[i]
    else:
      A[i] = ((A[i-1]>>T[i])<<T[i])|(1<<T[i])
      if A[i] <= A[i-1]:
        count = T[i]+1
        while A[i] <= A[i-1]:
          A[i] ^= 1<<count
          count += 1
  
  # print()
  # for i in range(N):
  #   print(f'{A[i]:040b}', T[i])
  print(A[-1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()