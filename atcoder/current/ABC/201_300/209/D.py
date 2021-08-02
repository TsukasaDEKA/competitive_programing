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
        input = """4 1
1 2
2 3
2 4
1 2"""
        output = """Road"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 2
1 2
2 3
3 4
4 5
1 3
1 5"""
        output = """Town
Town"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """9 9
2 3
5 6
4 8
8 9
4 5
3 4
1 9
3 7
7 9
2 5
2 6
4 6
2 4
5 8
7 8
3 6
5 6"""
        output = """Town
Road
Town
Town
Town
Town
Road
Road
Road"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  # クエリ先読みっぽいな
  # 木構造なので最短経路しか無いはず。
  # 距離が偶数なら Town、そうで無いなら Road
  # アルゴリズム名がわからん
  # ダブリング
  N, Q = map(int, input().split(" "))
  EDGE = [set() for _ in range(N)]
  for _ in range(N-1):
    a, b = [int(x)-1 for x in input().split(" ")]
    EDGE[a].add(b)
    EDGE[b].add(a)

  k = N.bit_length()
  # データの構築
  D = [[0]*N for _ in range(k)]
  D[0][0] = -1
  nexts = deque()
  nexts.append(0)
  checked = [False]*N
  checked[0] = True
  while nexts:
    current = nexts.popleft()
    for n in EDGE[current]:
      if checked[n]: continue
      checked[n] = True
      D[0][n] = D[0][current]+1
      nexts.append(n)

  # for i in range(k-1):
  #   for j in range(N):
  #     D[i+1][j]=D[i][D[i][j]]

  for i in range(Q):
    a, b = [int(x)-1 for x in input().split(" ")]
    # a の深さを求める
    d_a = D[0][a]
    d_b = D[0][b]
    if abs(d_a-d_b) % 2:
      print("Road")
    else:
      print("Town")
    # d_a = 0
    # c = a
    # while c != 0:
    #   D[]

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()