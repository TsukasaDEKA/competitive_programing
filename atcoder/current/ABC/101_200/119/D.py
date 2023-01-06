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
        input = """2 3 4
100
600
400
900
1000
150
2000
899
799"""
        output = """350
1400
301
399"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1 3
1
10000000000
2
9999999999
5000000000"""
        output = """10000000000
10000000000
14999999998"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # 二分探索をすると 東西それぞれの方向にあって最寄りの寺社がすぐわかりそう。
  # 例えば、s[i]-t[i]- x -s[i+1]-t[i+1] のような位置関係の時、
  # 神社・寺の組み合わせが、東東、西西、東西、西東 の 4 パターンある。
  # それぞれのパターンを正しく計算する必要がある。
  A, B, Q = map(int, input().split(" "))
  S = [-inf] + [int(input()) for _ in range(A)] + [inf]
  T = [-inf] + [int(input()) for _ in range(B)] + [inf]
  # T = [-inf] + [[int(input()) for _ in range(B)] + [inf]
  def binary_search(ok, ng, solve, x):
    mid = (ok+ng)//2
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, x): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok, x) else -1

  def s_solve(i, x):
    return S[i] < x
  
  def t_solve(i, x):
    return T[i] < x

  for _ in range(Q):
    x = int(input())
    s = binary_search(0, A+2, s_solve, x)
    t = binary_search(0, B+2, t_solve, x)
    ans = inf
    # 東東パターン
    ans = min(ans, max(S[s+1], T[t+1])-x)
    # 西西パターン
    ans = min(ans, x - min(S[s], T[t]))
    # 東西パターン
    ans = min(ans, 2*min(x-T[t], S[s+1]-x)+max(x-T[t], S[s+1]-x))
    # 西東パターン
    ans = min(ans, 2*min(x-S[s], T[t+1]-x)+max(x-S[s], T[t+1]-x))

    print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
