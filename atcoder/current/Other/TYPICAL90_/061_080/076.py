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

    def test_入力例_1(self):
        input = """10
1 1 1 1 1 1 1 1 1 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 1 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1 18 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4
1 9 1 9"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  # sum(A)/10, sum(A)*9/10 のどちらかが見つかればいい。
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  sumA = sum(A)
  integA = [0]*(N+1)
  for i in range(N):
    integA[i+1] = integA[i] + A[i]

  # メグル式二分探索。
  def binary_search(ok, ng, solve, offset, integA, tar):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, offset, integA, tar): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok, offset, integA, tar) else -1

  def solve(x, offset, integA, tar):
    return integA[x]-integA[offset] <= tar


  for i in range(1, N+1):
    j_p = binary_search(i, N+1, solve, i-1, integA, sumA/10)
    j_n = binary_search(i, N+1, solve, i-1, integA, sumA/10*9)
    if integA[j_p]-integA[i-1] == sumA/10 or integA[j_n]-integA[i-1] == sumA/10*9:
      print("Yes")
      return
  print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
