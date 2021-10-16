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
ababa"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
xy"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """13
strangeorange"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  # 答えは N//2 以下になる。
  # len を二分探索する？
  # lenX が答えの時 lenX-1 も答えを満たす。=> 二分探索可能
  N = int(input())
  S = list(input())

  # メグル式二分探索。
  def binary_search(ok, ng, solve):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok) else -1

  def solve(length):
    temp = defaultdict(list)
    for i in range(N-length+1):
      s = "".join(S[i:i+length])
      if s in temp:
        if temp[s][0] + length <= i:
          return True
      else:
        temp[s].append(i)
    return False

  ans = binary_search(1, N//2+1, solve)
  print(ans if ans >= 0 else 0)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()