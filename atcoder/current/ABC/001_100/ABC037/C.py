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

    def test_入力例_1(self):
        input = """5 3
1 2 4 8 16"""
        output = """49"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 10
100000000 100000000 98667799 100000000 100000000 100000000 100000000 99986657 100000000 100000000 100000000 100000000 100000000 98995577 100000000 100000000 99999876 100000000 100000000 99999999"""
        output = """10988865195"""
        self.assertIO(input, output)

def resolve():
  # 累積和
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  integral_A = [0]*(N+1)
  for i in range(N):
    integral_A[i+1] = integral_A[i] + A[i]
  
  ans = 0
  for right in range(K, N+1):
    left = right - K
    ans+= integral_A[right] - integral_A[left]
  print(ans)
resolve()

if __name__ == "__main__":
    unittest.main()
