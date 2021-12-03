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
        input = """5 7
1 2 2
1 4 1
2 3 7
1 5 12
3 5 2
2 5 3
3 4 5"""
        output = """13"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 4
1 2 1
1 3 1
1 4 1
1 5 1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 12
1 4 3
1 9 1
2 5 4
2 6 1
3 7 5
3 10 9
4 7 2
5 6 6
5 8 5
6 8 3
7 9 5
8 10 8"""
        output = """11"""
        self.assertIO(input, output)

def resolve():
  # 家 1 から伸びている 2 本の道は必ず通る事になる。
  # 逆に、2 本以上通るケースは必ずそれ以上に短い経路があるはずなので考えなくていい。
  # 家 1 に隣接する家を 2 つ選んでその 2 点の最短距離 + 家 1 までの道の長さを求める。
  # その長さの中で一番短いものが答え。
  # ダイクストラで考えてたけど、二点間の距離を求めるならワーシャルフロイドの方が良さそう。
  # O(N**3) だけど N <= 300 なので、 N**3 <= 27*(10**6) で十分間に合いそう。
  inf = 10**18+1
  N, M = map(int, input().split(" "))

  EDGE = [[inf]*N for _ in range(N)]

  query = sorted([[int(x) for x in input().split(" ")] for _ in range(M)])
  for i in range(M):
    u, v, l = query[i]
    u, v = min(u-1, v-1), max(u-1, v-1)
    EDGE[u][v] = l
    EDGE[v][u] = l
 
  # ワーシャルフロイドで 2 点間の距離を求める。
  ranges = range(1, N)
  for k in ranges:#経由点
    edge_k = EDGE[k]
    for i in ranges:#始点
      edge_i_k = EDGE[i][k]
      edge_i = EDGE[i]
      for j in range(i+1, N):#終点
        if i == j: continue
        edge_i[j] = EDGE[j][i] = min(edge_i[j], EDGE[j][i], edge_i_k+edge_k[j])

  # 全ての 2 点間の最短距離 + 家1と繋がっている道の距離 (家1と繋がっていない場合は inf ) を求めて最短のものを探す
  # 家 1 との隣接点だけを使えば計算量を減らせるけど、実装を減らしたかったので全ての 2 点の距離を求めている。
  ans = inf
  for i in range(N-1):
    for j in range(i+1, N):
      ans = min(ans, EDGE[i][j]+EDGE[0][j]+EDGE[i][0])

  print(ans if ans != inf else -1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()