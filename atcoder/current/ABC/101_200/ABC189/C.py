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
        input = """6
2 4 4 9 4 9"""
        output = """20"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
200 4 4 9 4 9"""
        output = """200"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
200 4 4 9 4 3"""
        output = """200"""
        self.assertIO(input, output)


def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  # seg = SegTree(A, segfunc, ide_ele)
 
  ans = 0
  right = [0]*N
  for i in reversed(range(N-1)):
    length = 1
    while A[i] <= A[i+length]:
      length+=1
      if i+length >= N: break
    right[i] = length-1

  left = [0]*N
  for i in range(1, N):
    length = 1
    while A[i] <= A[i-length]:
      length+=1
      if i-length < 0: break
    left[i] = length-1


  ans = 0
  for i in range(N):
    ans = max(ans, A[i]*(right[i]+left[i]+1))
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
