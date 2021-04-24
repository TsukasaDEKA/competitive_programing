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
        input = """3
1 2 2
2 3 1"""
        output = """0
0
1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
2 5 2
2 3 10
1 3 8
3 4 2"""
        output = """1
0
1
0
1"""
        self.assertIO(input, output)

from collections import deque

def resolve():
  # 端から順に探索していって、距離が偶数だったら同じ色にする、ってのを繰り返していけば良さそう。
  # UnionFind?
  # グラフを構築して、探索して、距離が偶数の 2 頂点を見つけたら Union していく感じ
  # o -偶数- o -偶数- o みたいな連結だったら問題ないんだけど、
  # o -奇数- o -奇数- o みたいな連結の時に先頭と末尾の距離計算が大変。累積和？
  # 全ての点は「根からの距離が偶数か奇数か」で塗り分けられる。
  # なので、幅優先探索していって、「根と同じ色かそうでないか」を求めれば良い。
  # 根は任意の点で良さそう。(本当か？) なので 0 を根にしてやってみる。
  N = int(input())
  routes = [[] for _ in range(N)]
  for _ in range(N-1):
    u, v, w = map(int, input().split(" "))
    u-=1
    v-=1
    routes[u].append((v, w))
    routes[v].append((u, w))
  
  distance_from_root = [0]*N
  next_node = deque([0])
  while next_node:
    current = next_node.popleft()
    for node, w in routes[current]:
      # print(w)
      if distance_from_root[node] == 0:
        distance_from_root[node] = distance_from_root[current] + w
        next_node.append(node)

  for d in distance_from_root:
    print(0 if d%2==0 else 1)
resolve()

if __name__ == "__main__":
    unittest.main()
