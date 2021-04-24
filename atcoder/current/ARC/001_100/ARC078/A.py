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
1 2 3 4 5 6"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
10 -10"""
        output = """20"""
        self.assertIO(input, output)

def resolve():
  # 累積和。二分探索したら早そうだけど、今回はしなくても間に合うっぽい
  inf = 10**10+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  integral_A = [0]*(N+1)
  for i in range(N):
    integral_A[i+1] = integral_A[i]+A[i]

  ans = inf
  for i in range(1, N):
    ans = min(ans, abs(integral_A[-1]-2*integral_A[i]))
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
