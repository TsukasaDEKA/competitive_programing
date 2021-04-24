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
-10 2
10 1
10 3
5
-15 -10 -5 0 5"""
        output = """0
0
5
10
10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
-10 3
10 1
10 2
5
-15 -10 -5 0 5"""
        output = """0
0
5
10
10"""
        self.assertIO(input, output)

def resolve():
  inf = 10**32
  # 上限、下限をずらす動作をする。
  N = int(input())
  max_ = inf
  min_ = -inf
  bias = 0
  for _ in range(N):
    A, T = map(int, input().split(" "))
    if T == 1:
      max_ += A
      min_ += A
      bias += A
    elif T == 2:
      if min_ < A:
        min_ = A
      if max_ < min_:
         max_ = min_
    elif T == 3:
      if max_ > A:
        max_ = A
      if min_ > max_:
         min_ = max_

  Q = int(input())
  X = [int(x) for x in input().split(" ")]
  for x in X:
    print(max(min_, min(max_, x+bias)))

resolve()

if __name__ == "__main__":
    unittest.main()
