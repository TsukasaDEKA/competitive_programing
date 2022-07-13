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

    def test_入力例_1(self):
        input = """5 2 3
1 2
3 4"""
        output = """1 2 3 4 5
1 3 2 4 5
1 3 5 2 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2 1
1 3
3 1"""
        output = """-1"""
        self.assertIO(input, output)

#     def test_入力例_3(self):
#         input = """10 15 10
# 8 4
# 9 4
# 10 2
# 6 2
# 10 6
# 1 3
# 7 4
# 6 8
# 8 1
# 5 6
# 10 9
# 3 7
# 8 3
# 3 9
# 2 3"""
#         output = """5 10 6 2 8 1 3 7 9 4
# 5 10 6 2 8 1 3 9 7 4
# 5 10 6 8 2 1 3 7 9 4
# 5 10 6 8 2 1 3 9 7 4
# 5 10 6 8 1 2 3 7 9 4
# 5 10 6 8 1 2 3 9 7 4
# 10 5 6 2 8 1 3 7 9 4
# 10 5 6 2 8 1 3 9 7 4
# 10 5 6 8 2 1 3 7 9 4
# 10 5 6 8 2 1 3 9 7 4"""
#         self.assertIO(input, output)

def resolve():
  # Ai -> Bi の有向辺を持つグラフだと考える。これが DAG で無い場合、答えは -1
  # のトポロジカルソートをして、辺を持たない点をその間に入れればできそう。
  # DAG 判定はトポロジカルソートと同時に行える。
  # K = 1 の場合、トポロジカルソートするだけで大丈夫。
  # 入出次数管理すればいけるか？
  # とりあえず トポロジカルソート してみてからデータを確認して考える。

  # https://atcoder.jp/contests/abc041/tasks/abc041_d
  # 似ている問題を見つけたけど、N の数が段違いなので応用できるかは微妙。
  from collections import defaultdict

  def topological_sort(N, in_degrees, outs):
    from collections import deque

    topological_graph = []
    # 入次数 0 のノードから始める。
    nexts = deque(x for x in range(N) if in_degrees[x] == 0)
    while nexts:
      current = nexts.popleft()
      topological_graph.append(current)
      for tar in outs[current]:
        in_degrees[tar]-=1
        # 入次数が 0 だったら追加する。
        if in_degrees[tar]==0: nexts.append(tar)

    return topological_graph

  # 小課題 1 は O(N**2) でもいける。
  N, M, K = map(int, input().split(" "))
  out_ = defaultdict(list)
  in_degrees = defaultdict(int)

  for _ in range(M):
    x, y = [int(x)-1 for x in input().split(" ")]
    out_[x].append(y)
    in_degrees[y]+=1

  topological_graph = topological_sort(N, in_degrees, out_)

  print(in_degrees)
  print(out_)

  print(topological_graph)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
