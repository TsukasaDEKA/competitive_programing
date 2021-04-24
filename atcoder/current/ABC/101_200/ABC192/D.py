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
        input = """22
10"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """999
1500"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100000000000000000000000000000000000000000000000000000000000
1000000000000000000"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10
2"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """100
2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_6(self):
        input = """3
4"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**24+1
  X = [int(x) for x in list(input())]
  M = int(input())

  start = max(X)+1
  len_X = len(X)
  ans = 0

  if len_X == 1:
    if X[0] <= M:
      print(1)
    else:
      print(0)
    return

  def solve(n):
    tar = 0
    for i in range(len_X):
      tar += X[i]*pow(n, len_X-i-1)
    return tar <= M

  if not solve(start):
    print(0)
    return
  # 二分探索
  ok = start
  ng = M+1
  mid = start
  while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if solve(mid):
      ok = mid
    else:
      ng = mid

  while not solve(mid):
    mid-=1
    if mid < start:
      print(0)
      return

  print(max(0, mid-start+1))

# resolve()

if __name__ == "__main__":
    unittest.main()
