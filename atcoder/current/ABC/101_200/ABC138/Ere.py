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
        input = """contest
son"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """contest
programming"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """contest
sentence"""
        output = """33"""
        self.assertIO(input, output)

def resolve():
  from bisect import bisect_left
  from collections import defaultdict

  # メグル式二分探索。
  def binary_search(ok, ng, solve, tar, agg):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, tar, agg): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok, tar, agg) else -1

  def solve(i, tar, agg):
    return agg[i] > tar

  S = list(input())
  T = list(input())
  N_S = len(S)
  N_T = len(T)

  agg_s = defaultdict(list)
  for i in range(N_S):
    agg_s[S[i]].append(i)

  ans = 0
  recent = -1
  for i in range(N_T):
    if T[i] not in agg_s:
      print(-1)
      return
    ok = len(agg_s[T[i]])-1
    ng = -1
    index = binary_search(ok, ng, solve, recent, agg_s[T[i]])

    if index == -1:
      ans += N_S - recent - 1
      recent = -1
      index = binary_search(ok, ng, solve, recent, agg_s[T[i]])

    ans += agg_s[T[i]][index]-recent
    recent = agg_s[T[i]][index]

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()