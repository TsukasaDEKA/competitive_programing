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
        input = """5 3
6 11 2 5 5
5
20
0"""
        output = """10
71
29"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 5
1000000000 314159265 271828182 141421356 161803398 0 777777777 255255255 536870912 998244353
555555555
321654987
1000000000
789456123
0"""
        output = """3316905982
2811735560
5542639502
4275864946
4457360498"""
        self.assertIO(input, output)

def resolve():
  from itertools import accumulate # 累積和作るやつ

  inf = 10**18+1
  N, Q = map(int, input().split(" "))
  A = sorted([int(x) for x in input().split(" ")])
  accA = list(accumulate(A))

  # メグル式二分探索。
  def binary_search(ok, ng, solve, X):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, X): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok, X) else -1

  def solve(i, X):
    return A[i] <= X

  for _ in range(Q):
    X = int(input())
    index = binary_search(0, N, solve, X)
    if index == -1:
      print(accA[-1]-X*N)
      continue
    less_count = index+1
    bigger_count = N - less_count

    ans = (X*less_count-accA[index]) + (accA[-1]-accA[index] - X*bigger_count)
    print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()