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

    def test_入力例1(self):
        input = """4
100 150 130 120"""
        output = """40"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4
100 125 80 110"""
        output = """40"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """9
314 159 265 358 979 323 846 264 338"""
        output = """310"""
        self.assertIO(input, output)

def resolve():
  # EDPC で見た気がする
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  DP = [0]*N
  DP[1] = abs(A[0]-A[1])
  for i in range(2, N):
    DP[i] = min(DP[i-1]+abs(A[i]-A[i-1]), DP[i-2]+abs(A[i]-A[i-2]))

  print(DP[-1])
resolve()

if __name__ == "__main__":
    unittest.main()
