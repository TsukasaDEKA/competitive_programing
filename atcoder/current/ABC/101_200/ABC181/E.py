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
        input = """5 3
1 2 3 4 7
1 3 8"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7 7
31 60 84 23 16 13 32
96 80 73 76 87 57 29"""
        output = """34"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """15 10
554 525 541 814 661 279 668 360 382 175 833 783 688 793 736
496 732 455 306 189 207 976 73 567 759"""
        output = """239"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  # 累積和 + 二分探索？
  # H を昇順ソートして i > j のようにペアをとるとすると、|xi - yj| == xi - yj になる。
  # 先生とペアになる児童を X 番目とする。
  # 答えは、 Xが奇数の時、(先生と児童Xの差) + ((1 ~ X-1 までの偶数番目の身長の和) + (X+1 ~ N までの奇数数番目の身長の和)) - ((1 ~ X-1 までの奇数番目の身長の和) + (X+1 ~ N までの偶数番目の身長の和)) になる。
  # (先生と児童Xの差)　以外の部分はソート後の H の偶数番目と奇数番目の累積和をそれぞれとっておくと O(1) で求まる。
  # あとは、児童 X の身長を H[X] とした時に、|W[i] - H[X]| が最小になる i を二分探索で見つければ良くて、
  # 計算量は O(N(累積和作成分) + N(Xを抜いたその他の児童のペアを作る作業)*log M (二分探索))なので間に合いそう。


  N, M = map(int, input().split(" "))
  H = sorted([int(x) for x in input().split(" ")])
  W = sorted([int(x) for x in input().split(" ")])

  # 偶奇で累積和
  # 添字バグらせそう。
  integral_odd_H = [0]*(N+1)
  integral_even_H = [0]*(N+1)
  for i in range(N):
    if i%2:
      integral_odd_H[i+1] = integral_odd_H[i]
      integral_even_H[i+1] = H[i]+integral_even_H[i]
    else:
      integral_odd_H[i+1] = H[i]+integral_odd_H[i]
      integral_even_H[i+1] = integral_even_H[i]

  def solve(teacher, x):
    return teacher < x

  # print(integral_odd_H, integral_even_H)
  ans = inf
  for x in range(N):
    # x 番目の児童と先生のペアを作る。
    # 二分探索
    min_x = inf
    ok = 0
    ng = M
    # メグル式上手く書けない。
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      min_x = min(min_x, abs(W[mid]-H[x]))
      if min_x == 0: break
      if solve(W[mid], H[x]):
        ok = mid
      else:
        ng = mid
    mid = (ok+ng)//2
    min_x = min(min_x, abs(W[mid]-H[x]))

    temp_ans = min_x + (integral_odd_H[-1]-integral_odd_H[x+1]) + integral_even_H[x] - (integral_odd_H[x] + ((integral_even_H[-1]-integral_even_H[x+1])))
    ans = min(ans, temp_ans)
    if ans == 0: break
  print(ans)
resolve()


if __name__ == "__main__":
    unittest.main()
