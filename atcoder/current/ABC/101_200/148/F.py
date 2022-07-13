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
        input = """5 4 1
1 2
2 3
3 4
3 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 4 5
1 2
1 3
1 4
1 5"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2 1 2
1 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """9 6 1
1 2
2 3
3 4
4 5
5 6
4 7
7 8
8 9"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """2 1 2
1 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_6(self):
        input = """3 2 3
1 2
2 3"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  # 高橋くんが移動できる頂点は、青木くんが最短距離で向かってきた時にすれ違わずに移動できる頂点全て
  # 先に青木くんから全ての点への距離を求める。
  # 次に、高橋くんから全ての点への距離を求めるが、青木くんの方が近い頂点については距離 0 にする。
  # また、葉の一個手前の頂点で合流することになる。
  # 頂点の一個手前かつ、
  inf = 10**18+1
  from collections import deque

  N, U, V = map(int, input().split(" "))

  U-=1
  V-=1
  EDGES = [[] for _ in range(N)]
  for _ in range(N-1):
    A, B = [int(x)-1 for x in input().split(" ")]
    EDGES[A].append(B)
    EDGES[B].append(A)

  nexts = deque()
  nexts.append(V)
  AOKI = [0]*N
  checked = [False]*N
  checked[V] = True
  while nexts:
    current = nexts.popleft()
    for n in EDGES[current]:
      if checked[n]: continue
      checked[n] = True
      AOKI[n] = AOKI[current]+1
      nexts.append(n)

  checked = [False]*N
  checked[U] = True
  TAKAHASHI = [0]*N
  nexts.append(U)
  while nexts:
    current = nexts.popleft()
    for n in EDGES[current]:
      if checked[n]: continue
      checked[n] = True
      if AOKI[n] <= TAKAHASHI[current]+1 and len(EDGES[current])!=1: continue
      TAKAHASHI[n] = TAKAHASHI[current]+1
      nexts.append(n)

  TAKAHASHI[U] = 1
  ans = 0
  for i in range(N):
    if TAKAHASHI[i] == 0: continue
    if len(EDGES[i]) == 1: continue
    ans = max(AOKI[i], ans)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()