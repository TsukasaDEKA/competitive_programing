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
        input = """3 4 2
0 3 -1
3 0 5
-1 5 0"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 10 2
0 -1 10
-1 0 1
10 1 0"""
        output = """Infinity"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """13 777 77
0 425 886 764 736 -1 692 660 -1 316 424 490 423
425 0 -1 473 -1 311 -1 -1 903 941 386 521 486
886 -1 0 605 519 473 775 467 677 769 690 483 501
764 473 605 0 424 454 474 408 421 530 756 568 685
736 -1 519 424 0 -1 804 598 911 731 837 459 610
-1 311 473 454 -1 0 479 613 880 -1 393 875 334
692 -1 775 474 804 479 0 579 -1 -1 575 985 603
660 -1 467 408 598 613 579 0 456 378 887 -1 372
-1 903 677 421 911 880 -1 456 0 859 701 476 370
316 941 769 530 731 -1 -1 378 859 0 800 870 740
424 386 690 756 837 393 575 887 701 800 0 -1 304
490 521 483 568 459 875 985 -1 476 870 -1 0 716
423 486 501 685 610 334 603 372 370 740 304 716 0"""
        output = """42"""
        self.assertIO(input, output)

def resolve():
  from copy import deepcopy
  # 無限個ってあり得るのか？
  # => あり得る。-1 のマスを通らないでも全ての i=>j の組み合わせにおいて P スヌークで移動できる。
  # X を三分探索する？
  # X を上げた時 => 条件を満たす組み合わせの数は同じか減る。
  # X を下げた時 => 条件を満たす組み合わせの数は同じか増える。
  # 条件を満たす組み合わせが K である X の範囲を求める。
  # 二分探索 2 回の方が良さそう。
  # ワーシャルフロイドを行うと、一回の探索で 64000 程度の計算を行うことになる。
  # X を探索する計算は log(10**9) == 30 程度なので、30*64000 程度でまぁ間に合いそう。
  # 実装しんど

  # メグル式二分探索。
  def binary_search(ok, ng, n, p, k, costs, solve, check):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, n, p, k, costs, check): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok, n, p, k, costs, check) else 0

  def solve(x, n, p, k, costs, check):
    # 条件を満たす経路が丁度 K 個あるか判定する。
    t_costs = deepcopy(costs)
    for i in range(n):
      for j in range(n):
        if t_costs[i][j] == -1: t_costs[i][j] = x

    ranges = range(n)
    for l in ranges:
      t_costs_l = t_costs[l]
      for i in ranges:
        t_costs_i_l = t_costs[i][l]
        t_costs_i = t_costs[i]
        for j in range(i+1, n):
          t_costs_i[j] = t_costs[j][i] = min(t_costs_i[j], t_costs[j][i], t_costs_i_l+t_costs_l[j])

    count = 0
    for i in range(n-1):
      for j in range(i+1, n):
        if t_costs[i][j] <= p: count+=1

    # print(x, count, k)
    return check(count, k)

  def max_x(count, k):
    return count >= k

  def min_x(count, k):
    return count > k

  MAX_P = 10**9+1
  N, P, K = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]

  max_X = binary_search(1, MAX_P+1, N, P, K, A, solve, max_x)
  min_X = binary_search(1, MAX_P+1, N, P, K, A, solve, min_x)
  # 全ての X で条件を満たす経路数が K より大きい or K 未満
  if min_X >= MAX_P or max_X == 0:
    print(0)
    return
  # X = MAX_P で条件を満たすということは、X がそれ以上でも成立する。
  # つまり無限に X を選べる。
  if max_X >= MAX_P:
    print("Infinity")
    return
  # print(max_X, min_X)
  print(max_X-min_X)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()