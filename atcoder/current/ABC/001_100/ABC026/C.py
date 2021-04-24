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

    def test_入力例1(self):
        input = """5
1
1
1
1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """7
1
1
2
2
3
3"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """6
1
2
3
3
2"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """10
1
2
3
4
5
6
7
8
9"""
        output = """1023"""
        self.assertIO(input, output)

import sys
sys.setrecursionlimit(500*500)

def resolve():
  inf = 10**10+1
  from collections import defaultdict
  # 再帰的に給料を求めていく
  N = int(input())
  B = defaultdict(set)
  for i in range(1, N):
    b = int(input())-1
    B[b].add(i)

  def solve(i):
    if i not in B: return 1
    min_salary = inf
    max_salary = 0
    for b in B[i]:
      b_salary = solve(b)
      min_salary = min(min_salary, b_salary)
      max_salary = max(max_salary, b_salary)
    return min_salary + max_salary + 1

  print(solve(0))

resolve()

if __name__ == "__main__":
    unittest.main()
