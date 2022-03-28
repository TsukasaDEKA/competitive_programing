import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """5
6
8
1
2
3"""
        output = """21"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
3
1
4
1
5
9"""
        output = """25"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
5
5
1"""
        output = """8"""
        self.assertIO(input, output)

def resolve():
  from collections import deque

  # 貪欲でいけるか・・・？
  # 取りうる手が 4 手あって、その最善手を選べば良さそう。
  N = int(input())
  A = deque(sorted([int(input()) for _ in range(N)]))
  # print(A)

  ans = 0
  l, r = A[0], A[0]
  A.popleft()
  for _ in range(N-1):
    if max(abs(r-A[0]), abs(l-A[0])) >= max(abs(r-A[-1]), abs(l-A[-1])):
      val = A.popleft()
      if abs(r-val) > abs(l-val):
        ans += abs(r-val)
        r = val
      else:
        ans += abs(l-val)
        l = val
    else:
      val = A.pop()
      if abs(r-val) > abs(l-val):
        ans += abs(r-val)
        r = val
      else:
        ans += abs(l-val)
        l = val

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()