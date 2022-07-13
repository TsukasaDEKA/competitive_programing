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
        input = """4 4
1 2
1 3
1 4
2 3
5
4 2
3 3
2 4
4 5
1 6"""
        output = """1
1
3
2
5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 20
1 3
7 8
5 8
2 3
7 10
6 7
4 7
9 5
6 5
2 9
4 2
5 7
3 10
4 8
1 8
10 8
5 3
9 1
7 3
2 1
10
3 5
2 2
8 9
5 3
8 2
3 9
7 1
7 1
8 4
6 8"""
        output = """1
5
1
9
3
3
9
1
1
1"""
        self.assertIO(input, output)

def resolve():
  # 例えば全部の頂点が結合していた場合、愚直に計算すると O(M*Q) の計算量がかかるので間に合わない。
  # 一旦クエリを先読みすることを考える。
  # クエリを先読みすると、クエリの同士の依存関係がわかる。
  # xi のクエリは頂点 xi 自身かその隣接点が過去に受けたクエリの色になる。
  # どのクエリがどのクエリに影響を受けたかを考える。
  # 
  N, M = map(int, input().split(" "))
  EDGE = [set() for _ in range(N)]
  for _ in range(M): 
    a, b = [int(x)-1 for x in input().split(" ")]
    EDGE[a].add(b)
    EDGE[b].add(a)

  # 変更を入れたノードを覚えておいて、その中で一番最後に実行されたノードを使う。
  color = [(1, 0)]*N
  checked = set()
  Q = int(input())
  for _ in range(Q):
    x, c = [int(x) for x in input().split(" ")]
    for n in EDGE[x]:
      if n not in checked: continue
      if 
      color[n] = c
    x -= 1
    print(color[x])
    color[x] = c

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()