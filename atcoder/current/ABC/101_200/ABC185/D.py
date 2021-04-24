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
        input = """5 2
1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """13 3
13 3 9"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 5
5 2 1 4 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1 0"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  from math import ceil
  inf = 10**10+1
  N, M = map(int, input().split(" "))

  if M==0:
    print(1)
    return

  if M==N:
    print(0)
    return

  A = [int(x)-1 for x in input().split(" ")]

  A.sort()
  min_diff = inf

  diff = [0]*(M+1)
  diff[0] = A[0]
  if diff[0]!=0: min_diff = A[0]
  diff[-1] = N-A[-1]-1
  if diff[-1]!=0: min_diff = min(min_diff, diff[-1])

  for i in range(1, M):
    diff[i] = A[i]-A[i-1]-1
    if diff[i]!=0: min_diff = min(min_diff, diff[i])
  k = min_diff

  ans = 0
  for d in diff:
    ans+=ceil(d/k)
    # print(ceil(d/k), d, k)

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
