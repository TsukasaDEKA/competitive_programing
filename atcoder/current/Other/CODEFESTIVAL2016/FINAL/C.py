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
        input = """4 6
3 1 2 3
2 4 2
2 4 6
1 6"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 4
2 1 2
2 1 2
1 3
2 4 3"""
        output = """NO"""
        self.assertIO(input, output)

def resolve():
  from collections import deque

  # サンプルから、距離が 2 個以上離れていてもコミュニケーションを取れる。
  # [人]+[言語] のような配列を作って、BFS すればできそう。
  N, M = map(int, input().split(" "))
  L = [[int(x)-1 for x in input().split(" ")][1:] for _ in range(N)]
  EDGES = [[] for _ in range(N+M)]
  for i in range(N):
    for l in L[i]:
      EDGES[i].append(l+N)
      EDGES[l+N].append(i)

  checked = [False]*(N+M)
  checked[0] = True
  nexts = deque()
  nexts.append(0)
  while nexts:
    current = nexts.popleft()
    for n in EDGES[current]:
      if checked[n]: continue
      checked[n] = True
      nexts.append(n)

  print("YES" if sum(checked[:N]) == N else "NO")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()