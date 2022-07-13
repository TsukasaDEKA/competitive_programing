import sys
from io import StringIO
from typing import Tuple
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
        input = """4
3 4
1 3
2 3
2 1"""
        output = """4
2
1
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 1
2 2
3 3"""
        output = """3
2
1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
3 4
4 5
1 1
5 1
3 2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6
5 5
2 4
6 6
5 2
1 3
4 1"""
        output = """1
5
3
6
4
2"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """10
5 1
3 9
7 8
9 3
3 7
10 10
3 5
4 7
1 1
6 6"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  # 最後にボール k を塗る場合、白いボールが k のみなので　Ak, Bk のどちらかに k が含まれている必要がある。
  # つまり「Ai, Bi のどちらかに i が含まれているアイテム」(仮に自己完結したボールと呼ぶ)を最後に塗る事になる。
  # また、それぞれに依存関係がある。
  # 例 1 だと 1 は [3, 4]に依存, 2 は[1, 3]に依存、3 は[2, 3]に依存 4は[2, 1]に依存となる。
  # これは有向グラフで表現できる。
  # 自己完結したボールを始点にして依存関係を辺にして DFS を行い、最後にそれを逆順に遡っていけば全てを黒く塗れる。
  # 上記の事から、全てのボールを黒く塗れないパターンは以下のようになる。
  # 1. 自己完結したボールが存在しない
  # 2. 始点から遡っていっても全てを黒く塗りつぶすことができない
  from collections import deque

  N = int(input())
  # 辺の構築と自己完結したボール (DFS の開始点) の確認。
  EDGES = [set() for _ in range(N)]
  nexts = deque()
  checked = [False]*N
  for i in range(N):
    a, b = [int(x)-1 for x in input().split(" ")]
    # 自己完結したボールを始点にするので、DFS で使う deque に最初に入れておく。
    if a == i or b == i:
      nexts.append(i)
      checked[i] = True
    # a, b は i に依存されているという事を表現する有向辺
    EDGES[a].add(i)
    EDGES[b].add(i)

  # DFS で依存関係を手繰りながら塗っていく。最後に逆順で出力する。
  ans = []
  while nexts:
    current = nexts.popleft()
    ans.append(current+1)
    for n in EDGES[current]:
      if checked[n]: continue
      checked[n] = True
      nexts.append(n)

  print(*ans[::-1], sep="\n") if len(ans) == N else print(-1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
