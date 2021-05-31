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
        input = """3 2
1 7 0
5 8 11
10 4 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3
1 2 3
4 5 6
7 8 9"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  # 高い低いは-1, 1 で表せる。
  # 一回の計算で K**2 しなきゃいけない。だけど、logN*K**2 なので間に合いそう。
  inf = 10**18+1
  N, K = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]
  max_A = 0
  for i in range(N):
    for j in range(N):
      max_A = max(max_A, A[i][j])
  # メグル式二分探索。
  def search_ans(ok, ng, solve):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok) else -1

  def solve(x):
    temp = [[1 if A[i][j] > x else 0 for j in range(N)] for i in range(N)]
    int_map = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
      for j in range(N):
        int_map[i+1][j+1] = temp[i][j] + int_map[i+1][j] + int_map[i][j+1] - int_map[i][j]

    s = ((K**2)//2)+1
    for i_ in range(N-K+1):
      for j_ in range(N-K+1):
        right_tail_i = i_+K
        right_tail_j = j_+K
        temp = int_map[right_tail_i][right_tail_j] - int_map[i_][right_tail_j] - int_map[right_tail_i][j_] + int_map[i_][j_]
        if temp < s:
          return True
    return False


  ok = max_A
  ng = -1
  ans = search_ans(ok, ng, solve)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
