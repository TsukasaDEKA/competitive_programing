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

#     def test_Sample_Input_1(self):
#         input = """1
# 1 R
# 2 G"""
#         output = """1"""
#         self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """1
# 1 B
# 2 B"""
#         output = """0"""
#         self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """10
# 585 B
# 293 B
# 788 B
# 222 B
# 772 G
# 841 B
# 115 R
# 603 G
# 450 B
# 325 R
# 851 B
# 205 G
# 134 G
# 651 R
# 565 R
# 548 B
# 391 G
# 19 G
# 808 B
# 475 B"""
#         output = """0"""
#         self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """9
585 B
293 B
788 B
222 B
772 G
841 B
772 R
603 G
450 B
325 R
851 B
205 G
134 G
851 R
565 R
548 B
391 G
475 B"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  from collections import defaultdict
  # 色が違っても可愛さが一緒であれば不満は 0
  # 色が同じならば必ず不満は 0
  # それぞれの色から 1 匹 or 0 匹を別の色と組ませる事になる。
  # 奇数は 2 色か 0 色
  N = int(input())
  A = [[x for x in input().split(" ")] for _ in range(2*N)]
  cToI = {"R": 0, "G": 1, "B": 2}
  agg = defaultdict(list)
  for val, c in A:
    agg[cToI[c]].append(int(val))

  for i in range(3):
    agg[i].sort()

  odd = []
  even = []
  for i in range(3):
    if len(agg[i])%2:
      odd.append(agg[i])
    else:
      even.append(agg[i])

  # 全部偶数だったら 0
  if len(even) == 3:
    print(0)
    return

  # 奇数が 2 色の場合の不満の最小値
  # メグル式二分探索。
  def binary_search(ok, ng, solve, tar, val):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, tar, val): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok, tar, val) else -1

  def solve(x, tar, val):
    return tar[x] <= val

  # 奇数色同士を組ませる場合の不満
  odd_0 = odd[0]
  odd_1 = odd[1]
  even = even[0]
  ans = inf
  for v in odd_0:
    if len(odd_1) == 1:
      ans = min(ans, abs(v-odd_1[0]))
    else:
      match = binary_search(0, len(odd_1), solve, odd_1, v)
      ans = min(ans, abs(v-odd_1[match]))
      if match+1 < len(odd_1): ans = min(ans, abs(v-odd_1[match+1]))
      if ans == 0: break

  if ans == 0 or len(even) == 0:
    print(ans)
    return

  # print(odd_0, odd_1, even, sep="\n")
  # 奇数色と偶数色のペアを 2 組作る場合
  # 奇数色から 2 個選んで最小マッチさせる
  # 二乗になる・・・
  # 偶数色が同じ色を選んでも良い。
  temp_0 = inf
  for v in odd_0:
    match = binary_search(0, len(even), solve, even, v)
    temp_0 = min(temp_0, abs(v-even[match]))
    if match+1 < len(even): temp_0 = min(temp_0, abs(v-even[match+1]))

  temp_1 = inf
  for v in odd_1:
    match = binary_search(0, len(even), solve, even, v)
    temp_1 = min(temp_1, abs(v-even[match]))
    if match+1 < len(even): temp_1 = min(temp_1, abs(v-even[match+1]))

  # print(even)
  # print(temp_1, temp_0)
  print(min(ans, temp_0+temp_1))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
