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
        input = """5
2
1
4
5
3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
0
0
0
0"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  # 単調増加である部分列の個数の最小値を出す問題。
  # A を先頭から見ていって、
  # 今まで作成した部分列の全ての末尾と同じか小さい => 新しい部分列を作る
  # 今まで作成した部分列の中で末尾の数字が新しい数字より小さいものがある => その中で最大の物を選んで追加
  # 部分列の末尾だけ管理すれば良い。
  # できるだけ小さい末尾を残したい => 末尾が新しい数字より小さい部分列の中で、最大の物に追加したい。
  # list で管理して二分探索？
  # 部分列の末尾のインデックスだけ覚えておいて、末尾じゃなくなったら -inf を入れる？
  # 中間挿入が遅いので TLE しそう。 => 挿入は先頭にしか行わないので大丈夫
  from collections import deque
  # メグル式二分探索。
  def binary_search(ng, ok, solve, lasts, n):
    mid = (ok+ng)//2
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, lasts, n): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    # これだと index out of range になる場合があるので注意
    return ok if solve(ok, lasts, n) else -1

  N = int(input())
  A = [int(input()) for _ in range(N)]

  def solve(x, lasts, n):
    return lasts[x] < n

  ele = deque()
  ele.append(A[0])

  for a in A[1:]:
    index = binary_search(len(ele), 0, solve, ele, a)
    if index == -1: ele.appendleft(a)
    else: ele[index] = a

  print(len(ele))

resolve()

if __name__ == "__main__":
    unittest.main()
