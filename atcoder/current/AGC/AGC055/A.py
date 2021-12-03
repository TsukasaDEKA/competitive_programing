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
        input = """2
ABCCBA"""
        output = """111222"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """8
AAAAAAAABCBCBCBCBCBCBCBC"""
        output = """111211241244"""
        self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """10
# AAAAABCAAABCAABBBBBBBBCCCCCCCC"""
#         output = """111112211113231111111311111111"""
#         self.assertIO(input, output)

#     def test_Sample_Input_4(self):
#         input = """1
# ABC"""
#         output = """111"""
#         self.assertIO(input, output)

debug = False
def resolve():
  from itertools import permutations
  # ABC, ACB, BAC, BCA, CAB, CBA の 6 パターンが存在する。
  # A, B, C の個数のそれぞれの累積和を作って、
  # A は S[:i], B は S[i:j]、 C は S[j:] 区間のものを全て使うとした時、
  # それぞれの個数が一致する i, j を求めたい。
  # おそらく 6 回やれば全ての要素がグルーピングされるようになってる。
  from bisect import bisect_left
 
  s_to_n = {"A": 0, "B": 1, "C": 2}
  N = int(input())
  S = [s_to_n[x] for x in list(input())]
  temp = [x for x in S]
  # メグル式二分探索。
  def binary_search(ok, ng, solve, integral, a, b, c):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, integral, a, b, c): ok = mid
      else: ng = mid
 
    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok, integral, a, b, c) else -1
 
  def solve(k, integral, a, b, c):
    i = bisect_left(integral[a], k)
    if i >= len(integral[a]): return False
 
    j = bisect_left(integral[b], k+integral[b][i])
    if j >= len(integral[b]): return False
 
    l = bisect_left(integral[c], k+integral[c][j])
    if l >= len(integral[c]): return False
    
    return True
 
  # 6 個 のグループに分けるのでループ 6 回
  ans = [-1]*(3*N)
  cnt = 0
  for label in range(1, 7):
    # 二分探索用に累積和を構築
    integral = [[0]*(3*N+1) for _ in range(3)]
    for i in range(3*N):
      for j in range(3):
        integral[j][i+1] += integral[j][i]
        if S[i] == j: integral[j][i+1] += 1
 
    k = 0
    a = b = c = 0
    for a_, b_, c_ in permutations(list(range(3))):
      # K を二分探索する。
      k_ = binary_search(0, 12*N, solve, integral, a_, b_, c_)
      if k_ > k:
        k = k_
        a, b, c = a_, b_, c_

    # 前から a に相当する値、後ろから c に相当する値を取っていって、
    # 余った区間から b に相当する値をとる。
    a_i = 0
    count = 0
    for i in range(3*N):
      if S[i] == a:
        ans[i] = label
        S[i] = -1
        count+=1
        if count >= k:
          a_i = i
          break
    
    c_i = 0
    count = 0
    for i in reversed(range(3*N)):
      if S[i] == c:
        ans[i] = label
        S[i] = -1
        count+=1
        if count >= k:
          c_i = i
          break

    count = 0
    for i in range(a_i, c_i):
      if S[i] == b:
        ans[i] = label
        S[i] = -1
        count+=1
        if count >= k:
          break

    cnt += k
    if cnt >= N: break

  print(*ans, sep="")
 
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  # debug = True
  unittest.main()