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
        input = """6 2 3 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """0 0 0 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """998244353 -10 -20 30"""
        output = """998244363"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """-555555555555555555 -1000000000000000000 1000000 1000000000000"""
        output = """444445"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # 最寄りの Si を求める。
  # 二分探索？
  X, A, D, N = map(int, input().split(" "))

  # メグル式二分探索。
  def binary_search(ok, ng, solve):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok) else -1

  def solve_1(x):
    return A+(x-1)*D <= X

  def solve_2(x):
    return A+(x-1)*D >= X
  
  if D >= 0:
    if X <= A:
      print(abs(X-A))
      return
    if X >= A+(N-1)*D:
      print(abs(X-(A+(N-1)*D)))
      return
    n = binary_search(1, N+1, solve_1)
    print(min(abs(X-(A+(n-1)*D)), abs(X-(A+(n)*D)), abs(X-(A+(n-2)*D)), abs(X-(A+(n+1)*D))))
  else:
    if X >= A:
      print(abs(X-A))
      return
    if X <= A+(N-1)*D:
      print(abs(X-(A+(N-1)*D)))
      return
    n = binary_search(1, N+1, solve_2)
    print(min(abs(X-(A+(n-1)*D)), abs(X-(A+(n)*D)), abs(X-(A+(n-2)*D)), abs(X-(A+(n+1)*D))))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()