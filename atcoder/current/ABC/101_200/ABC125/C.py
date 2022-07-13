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
        input = """3
7 6 8"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
12 15 18"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2
1000000000 1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  # 0 ~ Ai の小さい順から 1, 2 番目のどちらかまでの中に答えがある。
  # min(A) を素因数分解して全部割り算する、ってやると間に合わない。
  # 公約数をそれぞれ記録して行って、大きい順にソートする。
  from math import gcd
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  gcd_L = [0]*(N+1)
  gcd_R = [0]*(N+1)

  for i in range(N):
    gcd_L[i+1] = gcd(gcd_L[i], A[i])
    gcd_R[N-i-1] = gcd(gcd_R[N-i], A[N-i-1])
  ans = 0
  for i in range(N):
    ans = max(ans, gcd(gcd_L[i], gcd_R[i+1]))
  print(ans)
resolve()

if __name__ == "__main__":
    unittest.main()
