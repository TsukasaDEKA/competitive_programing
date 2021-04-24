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
        input = """3 13
3 2 7
4 8 9
1 6 5"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 165
82 94 21 65 28 22 61 80 81 79
93 35 59 85 96 1 78 72 43 5
12 15 97 49 69 53 18 73 6 58
60 14 23 19 44 99 64 17 29 67
24 39 56 92 88 7 48 75 36 91
74 16 26 10 40 63 45 76 86 3
9 66 42 84 38 51 25 2 33 41
87 54 57 62 47 31 68 11 83 8
46 27 55 70 52 98 20 77 89 34
32 71 30 50 90 4 37 95 13 100"""
        output = """348179577"""
        self.assertIO(input, output)

class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n

  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]

  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)

    if x == y:
      return

    if self.parents[x] > self.parents[y]:
      x, y = y, x

    self.parents[x] += self.parents[y]
    self.parents[y] = x

  def size(self, x):
    return -self.parents[self.find(x)]

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def members(self, x):
    root = self.find(x)
    return [i for i in range(self.n) if self.find(i) == root]

  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]


  def roots_with_size(self):
    return [(i, abs(x)) for i, x in enumerate(self.parents) if x < 0]

  def group_count(self):
    return len(self.roots())

  def all_group_members(self):
    return {r: self.members(r) for r in self.roots()}

  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def resolve():
  N, K = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]
  base = 998244353

  columns_connect = UnionFind(N)
  for from_i in range(N-1):
    for to_i in range(from_i+1, N):
      can_move = True
      for j in range(N):
        if A[to_i][j] + A[from_i][j] > K:
          can_move = False
          break
      if can_move:
        columns_connect.union(from_i, to_i)

  columns_pattarn = 1
  for union in columns_connect.roots_with_size():
    for times in range(1, union[1]+1):
      columns_pattarn *= times


  rows_connect = UnionFind(N)
  for from_j in range(N-1):
    for to_j in range(from_j+1, N):
      can_move = True
      for i in range(N):
        if A[i][to_j] + A[i][from_j] > K:
          can_move = False
          break
      if can_move:
        rows_connect.union(from_j, to_j)

  rows_pattarn = 1
  for union in rows_connect.roots_with_size():
    for times in range(2, union[1]+1):
      rows_pattarn *= times

  print(columns_pattarn*rows_pattarn%base)

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
    unittest.main()
