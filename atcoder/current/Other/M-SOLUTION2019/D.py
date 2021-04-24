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
        input = """5
1 2
2 3
3 4
4 5
1 2 3 4 5"""
        output = """10
1 2 3 4 5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
1 2
1 3
1 4
1 5
3141 59 26 53 59"""
        output = """197
59 26 3141 59 53"""
        self.assertIO(input, output)

def resolve():
  # できるだけ同じ大きさの数字を組み合わせたい。
  # C はソートが必要っぽい
  # どっちが親か子かは特に関係なくて、
  # より多くの頂点とつながっている順に大きい数字を並べれば良さそう。
  # 2 番目に多く頂点を持っている頂点が同率で何個かあった場合、
  # もしその中に一番大きい数字を入れたノードと隣接しているものがあれば
  # それに大きな数字を入れた方が良さそうだけど、とりあえずそれは無しで考えてみる。
  # WA が出たので考え直してみる。
  # 辺の値を基準に考えていったらどうだろう。
  # 必ず、 C の最大値以外の要素の合計になるかも？
  # max(C) をどこかの頂点に配置した時、max(C) に繋がる辺は C の中で二番目に大きい数字になる。
  # 深さ優先探索で大きい数字から置いていく？
  # 何処のノードからスタートしても結果は一緒になるのかってのが疑問だけど多分大丈夫。
  # 大きい順から選んだ時、親 >= 子の関係が成立して、その二つを結ぶ辺の値は必ず子のものになる。
  from collections import deque
  N = int(input())
  edge_map = [set() for _ in range(N)]
  for i in range(N-1):
    a, b = [int(x)-1 for x in input().split(" ")]
    edge_map[a].add(b)
    edge_map[b].add(a)
  C = deque(sorted([int(x) for x in input().split(" ")], reverse=True))

  ans = sum(C) - C[0]
  tree = [0]*N
  nexts = deque([0])
  checked = [False]*N
  checked[0] = True
  while C:
    current = nexts.pop()
    tree[current] = C.popleft()
    for n in edge_map[current]:
      if checked[n]: continue
      checked[n] = True
      nexts.append(n)
  print(ans)
  print(*tree)
resolve()

if __name__ == "__main__":
    unittest.main()
