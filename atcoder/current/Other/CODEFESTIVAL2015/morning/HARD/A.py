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
1 2 3 4 5"""
        output = """20"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """9
100000000 20 15 11 14 20 15 11 15"""
        output = """554"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  # 白を選ぶ時、一手前の黒を選んだ方が強制的に選ばれる。
  # 前 2 つと後ろ 2 つを良い感じに足し算して少ない方を選んでいけば良さそう。
  inf = 10**18+1
  N = int(input())
  A = deque([int(x) for x in input().split(" ")])

  ans = 0
  for i in range(N//2):
    left = 2*A[0] + A[1] + 1
    tail = 2*A[-1] + A[-2] + 1
    if left < tail:
      ans += left
      temp = A.popleft() + A.popleft() + 2
      A[0] += temp
    else:
      ans += tail
      temp = A.pop() + A.pop() + 2
      A[-1] += temp
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()