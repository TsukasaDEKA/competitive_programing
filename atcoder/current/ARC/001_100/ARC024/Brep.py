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
        input = """5
0
1
1
1
0"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
1
1
0
1
1
1"""
        output = """3"""
        self.assertIO(input, output)


    def test_Sample_Input_3(self):
        input = """3
1
1
1"""
        output = """-1"""
        self.assertIO(input, output)



def resolve():
  N = int(input())
  A = [int(input()) for _ in range(N)]
  max_ = 0
  count = [1]*(2*N)
  for i in range(2*N):
    if A[(i%N)-1] == A[i%N]:
      count[i]+=count[i-1]
      max_ = max(max_, count[i])

  if max_ >= 2*N:
    print(-1)
    return
  print(max((max_+1)//2, 0))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()