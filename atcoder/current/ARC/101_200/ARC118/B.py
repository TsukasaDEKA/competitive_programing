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

    def test_入力例_1(self):
        input = """3 7 20
1 2 4"""
        output = """3 6 11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3 100
1 1 1"""
        output = """34 33 33"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 10006 10
10000 3 2 1 0 0"""
        output = """10 0 0 0 0 0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """7 78314 1000
53515 10620 7271 3817 1910 956 225"""
        output = """683 136 93 49 24 12 3"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+9
  from math import ceil, floor
  # メグル式二分探索。
  def binary_search(ok, ng, solve, A, N, M):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, A, N, M): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok, A, N, M) else -1

  def solve(x, A, N, M):
    L = [-(-(M*a-x)//N) for a in A]
    R = [(M*a+x)//N for a in A]
    # print(sum(L), sum(R), x, sum(L) <= M and M <= sum(R))
    return sum(L) <= M and M <= sum(R)

  # ceil((Ai-X)/N) <= Bi <= floor((Ai+X)/N) (i: 1~K) なる Bi となる最小の X を二分探索で求める。
  # Bi が存在する条件は sum(ceil((Ai-X)/N)) <= M <= sum(floor((Ai+X)/N))
  K, N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  X = binary_search(inf, -1, solve, A, N, M)

  B = [-(-(M*a-X)//N) for a in A]
  R = [(M*a+X)//N for a in A]
  dist = M-sum(B)
  for i in range(K):
    temp = min(dist, max(0, R[i]-B[i]))
    B[i] += temp
    dist -= temp

  print(*B)

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()
