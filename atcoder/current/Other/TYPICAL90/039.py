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
        input = """2
1 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2
1 3
1 4"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12
1 2
3 1
4 2
2 5
3 6
3 7
8 4
4 9
10 5
11 7
7 12"""
        output = """211"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  # 特定の辺は、子の頂点が持つ子の個数*(N-子の個数)回通過することになる。
  # 例えば、1-2, 1-3, 3-4 のような構造だと、1-3 を通る回数は 4 回 ((1,2) -> (3, 4) の時に通過する。)
  # 葉に繋がった辺を通る回数は必ず N-1 回になる。
  # 深さ優先探索で帰り際に持ってる子の数を置いていく
  # 根は計算から除外する。
  N = int(input())
  EDGES = [set() for _ in range(N)]
  for _ in range(N-1):
    A, B = [int(x)-1 for x in input().split(" ")]
    EDGES[A].add(B)
    EDGES[B].add(A)
  
  nexts = deque([0])
  checked = [False]*N
  checked[0] = True
  child_count = [0]*N
  while nexts:
    current = nexts.pop()

    if current < 0:
      child_count[-current] += 1
      for e in EDGES[-current]:
        child_count[-current] += child_count[e]
      continue

    count = 0
    for e in EDGES[current]:
      if checked[e]: continue
      checked[e] = True
      nexts.append(-e)
      nexts.append(e)

  ans = 0
  for i in range(1, N):
    ans += child_count[i]*(N-child_count[i])
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
