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

#     def test_Sample_Input_1(self):
#         input = """5 5
# 1 2
# 2 3
# 3 4
# 4 2
# 4 5"""
#         output = """4"""
#         self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 2
1 2
2 1
"""
        output = """2"""
        self.assertIO(input, output)


def resolve():
  # 注：対象になる = その頂点から開始した場合に無限に移動することが可能であるということ。
  # 行き止まり (出次数が 0 ) な頂点から開始した場合、そこから動けないので対象から外れる。
  # 行き止まりの一個手前の頂点について、行き止まりにしか移動できないのであればその頂点も対象から外れる。
  # 出次数を管理し、全ての行き止まりから遡る動作を行う。
  # 行き止まりから遡ってきたタイミングで出次数を減らし、その時点で出次数が 0 であれば対象外にする。
  # 出次数が 1 以上であればまだ対象になる可能性がある。
  # 他の行き止まりから遡ってきた場合、その頂点は対象外になる。
  # 逆に、他の行き止まりから遡ってくることがなかった場合、その頂点は対象になる。
  from collections import deque
  N, M = map(int, input().split(" "))

  # 逆向にした有向辺
  REV_EDGES = [[] for _ in range(N)]
  # 出次数
  OUT_DEGREE = [0]*N
  for _ in range(M):
    u, v = [int(x)-1 for x in input().split(" ")]
    REV_EDGES[v].append(u)
    OUT_DEGREE[u] += 1

  # 全ての頂点の個数から対象外になった頂点個数を引いていく。
  ans = N
  # 出次数が 0 の全ての頂点 (行き止まり) を BFS の開始点にする。
  nexts = deque([i for i, x in enumerate(OUT_DEGREE)  if x == 0])
  while nexts:
    current = nexts.popleft()
    # nexts (探索対象) に入る条件が出次数 0 であることなので、対象外であることは確定している。
    ans -= 1

    for n in REV_EDGES[current]:
      # 行き止まりから遡ってきたタイミングで出次数を出次数を 1 減らす
      OUT_DEGREE[n] -= 1
      # 出次数が 1 以上残っている場合、そこで遡るのを止める (別の行き止まりから遡ってくる場合はある。)
      if OUT_DEGREE[n]: continue
      nexts.append(n)
  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()