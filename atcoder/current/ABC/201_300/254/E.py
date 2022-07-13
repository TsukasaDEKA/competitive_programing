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
        input = """6 5
2 3
3 4
3 5
5 6
2 6
7
1 1
2 2
2 0
2 3
4 1
6 0
4 3"""
        output = """1
20
2
20
7
6
20"""
        self.assertIO(input, output)

def resolve():
  from collections import deque

  inf = 10**18+1
  # k が 3 以下なので普通に BFS すれば良さそう？
  N, M = map(int, input().split(" "))

  EDGES = [[] for _ in range(N)]
  for _ in range(M):
    A, B = [int(x)-1 for x in input().split(" ")]
    EDGES[A].append(B)
    EDGES[B].append(A)

  Q = int(input())
  for _ in range(Q):
    X, K = [int(x) for x in input().split(" ")]
    X -= 1

    ans = 0
    # ここから BFS
    checked = set([X])
    nexts = deque()
    nexts.append((X, 0))
    while nexts:
      current, step = nexts.popleft()
      ans+=current+1
      for e in EDGES[current]:
        if e in checked: continue
        checked.add(e)
        if step >= K: continue
        nexts.append((e, step+1))
    print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()