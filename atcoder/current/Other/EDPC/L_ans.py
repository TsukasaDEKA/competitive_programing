# https://atcoder.jp/contests/dp/tasks/dp_l
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
10 80 90 30"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
10 100 10"""
        output = """-80"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
10"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10
1000000000 1 1000000000 1 1000000000 1 1000000000 1 1000000000 1"""
        output = """4999999995"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """6
4 2 9 7 1 5"""
        output = """2"""
        self.assertIO(input, output)

import sys
sys.setrecursionlimit(500*500)

from numba import njit
@njit


def resolve():
inf = 10**10+1
N = int(input())
A = tuple([int(x) for x in input().split(" ")])

memo = [[None]*(N+1) for _ in range(N+1)]
def solve(i, j):
  if i == j:
    return A[i]
  elif memo[i][j] is not None:
    return memo[i][j]
  else: 
    left  = solve(i+1, j) if memo[i+1][j] is None else memo[i+1][j]
    right = solve(i, j-1) if memo[i][j-1] is None else memo[i][j-1]

    memo[i][j] = max(A[i] - left, A[j] - right)
    return memo[i][j]

print(solve(0, N-1))

# resolve()

if __name__ == "__main__":
    unittest.main()
