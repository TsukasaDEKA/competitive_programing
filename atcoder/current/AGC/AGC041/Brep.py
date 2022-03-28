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
        input = """6 1 2 2
2 1 1 3 0 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 1 5 2
2 1 1 3 0 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 4 8 5
7 2 3 6 1 6 5 4 6 5"""
        output = """8"""
        self.assertIO(input, output)

#     def test_Sample_Input_4(self):
#         input = """6 1 2 2
# 2 1 1 1 1 1"""
#         output = """6"""
#         self.assertIO(input, output)


def resolve():
  # メグル式二分探索。
  def binary_search(ok, ng, solve, V, M, A, border):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, V, M, A, border): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok

  def solve(x, V, M, A, border):
    if A[x]+M < A[border]: return False
    if A[x] >= A[border]: return True


    v = V - border - (N-x)
    if v <= 0: return True
    return (A[x]+M)*(x-border) - sum(A[border:x]) >= v*M

  # 答えで二分探索？
  # 上位 P-1 及び P 番目の問題と同着の問題は必ず採用される。
  inf = 10**18+1
  N, M, V, P = map(int, input().split(" "))
  A = sorted([int(x) for x in input().split(" ")], reverse=True)

  border = A.index(A[P-1])
  print(binary_search(0, N, solve, V, M, A, border)+1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()