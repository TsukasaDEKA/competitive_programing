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

    # def test_Sample_Input_1(self):
    #     input = """3 7"""
    #     output = """2"""
    #     self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 10
"""
        output = """12
"""
        self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """1 1000000"""
    #     output = """392047955148"""
    #     self.assertIO(input, output)


def resolve():
  # https://atcoder.jp/contests/abc206/editorial/2129
  L, R = map(int, input().split(" "))
  L = max(2, L)
  def f1(l, r):
    return ((r-l+1)*(r-l))//2

  from collections import defaultdict
  # f2 => g 
  memo = [defaultdict(int) for _ in range(R+1)]
  def f2(l, r):
    if l == r: return 0
    # print(l, r)
    if memo[r][l] != 0: return memo[r][l]
    temp = 0
    for i in range(2, r):
      temp += f2((l-1)//i+1, r//i)
    # print(l, r, f1(l, r) - temp)
    memo[r][l] = f1(l, r) - temp
    return memo[r][l]

  f3 = sum([R//i-1 for i in range(L, R+1)])

  ans = 2*(f1(L, R) - f2(L, R) - f3)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
