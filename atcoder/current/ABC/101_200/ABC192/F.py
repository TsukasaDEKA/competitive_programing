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
        input = """3 9999999999
3 6 8"""
        output = """4999999994"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1000000000000000000
1"""
        output = """999999999999999999"""
        self.assertIO(input, output)

def resolve():
  # A の合計値が X を超えるのはありえない
  # 1 <= N <= 100 (つまり、1 <= k <= 100)
  # dp っぽいけどよくわからん。
  from collections import Counter
  inf = 10**10+1
  N, X = map(int, input().split(" "))
  A = Counter([int(x) for x in input().split(" ")])

  dp = [[] for _ in range(N+1)]

  print()

# resolve()

if __name__ == "__main__":
    unittest.main()
