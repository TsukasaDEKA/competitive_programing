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
        input = """4 3
1 2
2 3
3 4"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 4
1 2
1 3
1 4
4 5"""
        output = """48"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """16 22
12 1
3 1
4 16
7 12
6 2
2 15
5 16
14 16
10 11
3 10
3 13
8 6
16 8
9 12
4 3"""
        output = """271414432"""
        self.assertIO(input, output)

def resolve():
  mod = 10**9+7
  from collections import deque

  # 0 から BFS していくが、その時に場合数を計算していく。
  # 一直線であれば、根は K パターンに塗れる。
  # 根の子の一個めは K-1 パターンに塗れるが、根の子の二個目は K-2 パターンになる。
  # 根の子の i 個目は K-i パターンになる。
  # 全部の場合数を求めたらそれを全部掛け合わせると良い。
  N, K = map(int, input().split(" "))
  EDGES = [[] for _ in range(N)]
  for _ in range(N-1):
    U, V = [int(x)-1 for x in input().split(" ")]
    EDGES[U].append(V)
    EDGES[V].append(U)

  depth = [0]*N
  nexts = deque()
  nexts.append(0)
  pattarn = [0]*N
  pattarn[0] = K
  checked = [False]*N
  checked[0] = True
  while nexts:
    current = nexts.popleft()
    count = min(depth[current]+1, 2)
    for n in EDGES[current]:
      if checked[n]: continue
      checked[n] = True
      depth[n] = depth[current]+1
      pattarn[n] = K-count
      nexts.append(n)
      count += 1

  ans = 1
  for p in pattarn:
    ans*=p
    if ans >= mod: ans%=mod
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()