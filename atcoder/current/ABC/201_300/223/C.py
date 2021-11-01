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
        input = """3
1 1
2 1
3 1"""
        output = """3.000000000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 3
2 2
3 1"""
        output = """3.833333333333333"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
3 9
1 2
4 6
1 5
5 3"""
        output = """8.916666666666668"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  from bisect import bisect_left
  # 秒に変換して考える。

  N = int(input())
  lines = deque()
  sum_time = 0.0
  for i in range(N):
    A, B = [int(x) for x in input().split(" ")]
    lines.append([A, B])
    sum_time+=A/B
  target_time = sum_time/2

  ans = 0
  A, B = lines.popleft()
  while target_time > A/B:
    ans+=A
    target_time-=A/B
    A, B = lines.popleft()
  ans += target_time*B
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()