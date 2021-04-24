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
        input = """5 3 2
5 1 4 2 3"""
        output = """0
8
11
13
15"""
        self.assertIO(input, output)
import heapq
def resolve():
  mod = 10**9+7
  N, A, B = map(int, input().split(" "))
  X = [int(x) for x in input().split(" ")]

  K = []
  heapq.heapify(K)
  heapq.heappush(K, X[0])
  Y = X[0]
  print(0)

  for i in range(1, N):
    heapq.heappush(K, X[i])
    print(K, K[-1])
  # 最小二乗法的な解き方？


# resolve()

if __name__ == "__main__":
  unittest.main()