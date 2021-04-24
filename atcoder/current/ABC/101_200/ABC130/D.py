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
        input = """4 10
6 1 2 7"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 5
3 3 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 53462
103 35322 232 342 21099 90000 18843 9010 35221 19352"""
        output = """36"""
        self.assertIO(input, output)

def resolve():
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  integra_A = [0]*(N+1)
  for i in range(N):
    integra_A[i+1] = integra_A[i] + A[i]

  count=0
  for i in range(N):
    if integra_A[N] - integra_A[i] < K: break
    # 二分探索
    left = i
    right = N
    current = int((right+left)/2)
    while left != current and right != current:
      if integra_A[current] - integra_A[i] >= K: right = current 
      else: left = current
      current = int((right+left)/2)

    count += N-current
  print(count)

resolve()

if __name__ == "__main__":
    unittest.main()
