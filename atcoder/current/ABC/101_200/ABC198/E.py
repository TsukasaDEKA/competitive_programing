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
        input = """6
2 7 1 8 2 8
1 2
3 6
3 2
4 3
2 5"""
        output = """1
2
3
4
6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10
3 1 4 1 5 9 2 6 5 3
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10"""
        output = """1
2
3
5
6
7
8"""
        self.assertIO(input, output)

def resolve():
  from collections import deque, defaultdict
  from copy import deepcopy
 
  # 再帰の DFS でやる
  N = int(input())
  C = [int(x)-1 for x in input().split(" ")]
  PATH = [set() for _ in range(N)]
  for _ in range(N-1):
    a, b = [int(x)-1 for x in input().split(" ")]
    PATH[a].add(b)
    PATH[b].add(a)
  
  checked = [False]*N
  checked[0] = True
  color_count = [0]*(10**5)
  good = [False]*N

  def dfs(i):
    if color_count[C[i]]==0:
      good[i] = True

    color_count[C[i]]+=1

    for n in PATH[i]:
      if checked[n]: continue
      checked[n] = True
      dfs(n)

    color_count[C[i]] -= 1
  dfs(0)
  print(*[i+1 for i, x in enumerate(good) if x], sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  sys.setrecursionlimit(500*500)
  resolve()


if __name__ == "__main__":
    unittest.main()
