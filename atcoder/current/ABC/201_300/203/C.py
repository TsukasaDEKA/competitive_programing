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
        input = """2 3
2 1
5 10"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 1000000000
1 1000000000
2 1000000000
3 1000000000
4 1000000000
5 1000000000"""
        output = """6000000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 2
5 5
2 1
2 2"""
        output = """10"""
        self.assertIO(input, output)


def resolve():
  from collections import defaultdict
  inf = 10**18+1
  N, K = map(int, input().split(" "))
  money = defaultdict(int)
  A = sorted([[int(x) for x in input().split(" ")] for _ in range(N)])

  f = 0
  current = 0
  next_ = 0
  while True:
    next_ = K+current
    current = next_
    K = 0
    if f < N:
      while A[f][0] <= next_:
        K+=A[f][1]
        f+=1
        if f >= N: break
    if K <= 0:
      break
  print(current)

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()
