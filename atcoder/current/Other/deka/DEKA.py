import sys
from io import StringIO
import unittest

# class TestClass(unittest.TestCase):
#     def assertIO(self, input, output):
#         stdout, stdin = sys.stdout, sys.stdin
#         sys.stdout, sys.stdin = StringIO(), StringIO(input)
#         resolve()
#         sys.stdout.seek(0)
#         out = sys.stdout.read()[:-1]
#         sys.stdout, sys.stdin = stdout, stdin
#         self.assertEqual(out, output)

#     def test_Sample_Input_1(self):
#         input = """DEKAKDAEKDEKA"""
#         output = """12"""
#         self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """DEKAEKA"""
#         output = """-1"""
#         self.assertIO(input, output)

def resolve():
  # メグル式二分探索。
  def binary_search(ok, ng, solve, t, table):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, t, table): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok, t, table) else -1
  
  def solve(x, t, table):
    return table[x] > t

  from collections import defaultdict

  DEKA = list("DEKA")
  S = list(input())
  N = len(S)
  agg = defaultdict(list)
  for i in range(N):
    agg[S[i]].append(i)

  for c in DEKA:
    if len(agg[c]) < 2:
      print(-1)
      return

  # 先に先頭の D と A を決める。
  D = agg["D"]
  E = agg["E"]
  K = agg["K"]
  A = agg["A"]

  # 1 つめの A を決めて、2 つ目の D を決めて、その間に E と K が存在するか判定する。
  ans = -1
  for A_i in A[:-1]:
    if D[0] > A_i: continue

    # A_i 以上の最小の d インデックスを探す。
    d_1 = binary_search(len(D)-1, 0, solve, A_i, D)
    if d_1 == -1: break

    # D[0] 以上の最小の e インデックスを探す。
    e_0 = binary_search(len(E)-1, -1, solve, D[0], E)
    if e_0 == -1: continue
    if E[e_0] > A_i: continue

    # E[e_0] 以上の最小の k インデックスを探す。
    k_0 = binary_search(len(K)-1, -1, solve, E[e_0], K)
    if k_0 == -1: continue
    if K[k_0] > A_i: continue

    # D[d_1] 以上の最小の e インデックスを探す。
    e_1 = binary_search(len(E)-1, e_0,  solve, D[d_1], E)
    if e_1 == -1: continue
    if E[e_1] > A[-1]: continue

    # E[e_1] 以上の最小の k インデックスを探す。
    k_1 = binary_search(len(K)-1, k_0, solve, E[e_1], K)
    if k_1 == -1: continue
    if K[k_1] > A[-1]: continue

    
    temp = (A_i-D[0]+1)+(A[-1]-D[d_1]+1)
    if ans < temp:
      ans = max(ans, temp)

  print(ans if ans > 0 else -1)

import sys
if sys.argv[-1] == './DEKA.py':
  resolve()

# if __name__ == "__main__":
#   unittest.main()