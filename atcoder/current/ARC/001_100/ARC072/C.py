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
        input = """4
1 -3 1 0"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
3 -6 4 -5 7"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
-1 4 3 2 -5 4"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """4
0 1 -1 0"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  # 左から見ていって、条件を満たす値を愚直にとっていけばいける？(未証明)
  # 1, -2, -100000 とかのケースで WA になる。
  # 先頭を負にするケースと正にするケースで分けて考える。
  inf = 10**18
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  def solve(recent_val, A):
    ans = abs(A[0]-recent_val)
    current_val = recent_val
    for i in range(1, N):
      current_val+=A[i]
      # 条件を満たさない場合
      if recent_val*current_val >= 0:
        # 逆符号
        direction = (-recent_val)//abs(recent_val)
        diff = abs(current_val-direction)
        ans += diff
        current_val = direction
      recent_val = current_val
    return ans

  ans = inf
  ans = min(ans, solve(max(1, A[0]), A))
  ans = min(ans, solve(min(-1, A[0]), A))
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()