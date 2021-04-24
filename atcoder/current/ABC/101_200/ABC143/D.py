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
        input = """4
1 2 3 4"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 1000 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
218 786 704 233 645 728 389"""
        output = """23"""
        self.assertIO(input, output)

def resolve():
  # ソートして小さい方から a, b, c と取っていって、式が成り立つものを探していく。
  N = int(input())
  L = sorted([int(x) for x in input().split(" ")])

  def solve(mid, a, b):
    return L[mid] < L[a] + L[b]

  ans = 0
  for a in range(N-2):
    for b in range(a+1, N-1):
      ok = b+1
      ng = N
      while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if solve(mid, a, b):
          ok = mid
        else:
          ng = mid
      mid = (ok+ng)//2
      if L[mid] >= L[a] + L[b]: continue
      ans += (mid-b)
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
