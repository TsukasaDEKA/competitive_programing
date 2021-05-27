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
        input = """7
1 1 2 2 4 2
4
1 2
7 2
4 1
5 5"""
        output = """3
1
0
0"""
        self.assertIO(input, output)

def resolve():
  # それぞれのノードの深さを記録しておく
  # 各ノードのにその子の深さを記録していきたい。
  # DAG だよね。
  # トポロジカルソートされた状態
  # 最初の探索で重さ == 深さで経路を足していくか。
  inf = 10**18+1
  from collections import defaultdict, deque
  N = int(input())
  P = [int(x)-1 for x in input().split(" ")]
  EDGES = [set() for _ in range(N)]
  for i in range(N-1):
    EDGES[P[i]].add(i+1)
  agg_by_depth = [[] for _ in range(N)]

  nexts = deque()
  nexts.append(0)
  depth = [0]*N
  max_depth = 0
  time = 0
  in_ = [0]*N
  out_ = [0]*N
  while nexts:
    current = nexts.pop()
    if current < 0:
      out_[-current] = time
      time+=1
      continue

    agg_by_depth[depth[current]].append(time)
    in_[current] = time
    time+=1
    for n in EDGES[current]:
      depth[n] = depth[current]+1
      max_depth = max(max_depth, depth[n])

      nexts.append(-n)
      nexts.append(n)

  out_[0] = time
  for i in range(N):
    agg_by_depth[i].sort()

  def binary_search(ok, ng, solve, tar, val):
    # print(ok, ng, val)
    # return 0
    mid = (ok+ng)//2
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, tar, val): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok, tar, val) else -1

  def solve_in(x, tar, in_):
    return in_ <= tar[x]

  def solve_out(x, tar, out_):
    return tar[x] < out_

  # print(in_)
  # print(out_)
  Q = int(input())
  for _ in range(Q):
    U, D = [int(x) for x in input().split(" ")]
    U -= 1
    in_p = in_[U]
    out_p = out_[U]

    # 二分探索していく。
    if len(agg_by_depth[D]) == 0:
      print(0)
      continue
    in_result = binary_search(len(agg_by_depth[D])-1, -1, solve_in, agg_by_depth[D], in_p)
    out_result = binary_search(0, len(agg_by_depth[D]), solve_out, agg_by_depth[D], out_p)

    if in_result < 0 or out_result < 0:
      print(0)
      continue
    print(max(0, out_result-in_result+1))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
