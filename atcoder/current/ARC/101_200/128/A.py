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
3 5 2"""
        output = """0 1 1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
1 1 1 1"""
        output = """0 0 0 0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
426877385 186049196 624834740 836880476 19698398 709113743 436942115 436942115 436942115 503843678"""
        output = """1 1 0 1 1 1 1 0 0 0"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  tar = []
  temp = 0
  i = 0
  while i < N-1:
    i += 1
    if A[i] == A[temp]: continue
    if A[i] > A[temp]:
      temp = i
    elif A[i] < A[temp]:
      if i+1 < N:
        while A[i] > A[i+1]:
          i+=1
          if i+1 >= N: break
      tar.append(temp)
      tar.append(i)
      temp = i+1

  ans = [0]*N
  for i in tar:
    ans[i] = 1
  print(*ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()