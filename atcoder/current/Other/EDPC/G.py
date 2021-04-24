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
        input = """4 5
1 2
1 3
3 2
2 4
3 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 3
2 3
4 5
5 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 8
5 3
2 3
2 4
5 2
5 1
1 4
4 3
1 3"""
        output = """3"""
        self.assertIO(input, output)

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

def resolve():
  from collections import defaultdict, deque
  import sys
  sys.setrecursionlimit(500*500)

  N, M = map(int, input().split(" "))
  # 葉から順に遡っていって DP していく。
  # そのまま遡っていくと計算順序ずれる (親より子を先に計算する必要がある。)ため、先にトポロジカルソートする。
  # in_ = defaultdict(list)
  out_ = defaultdict(list)
  in_degrees = defaultdict(int)

  for _ in range(M):
    x, y = [int(x)-1 for x in input().split(" ")]
    # in_[y].append(x)
    out_[x].append(y)
    in_degrees[y]+=1

  # トポロジカルソートする。
  topological_graph = topological_sort(N, in_degrees, out_)

  # ここから DP
  # メモ化再帰関数
  def memo_recursion(memo, checked, index, outs):
    if not checked[index]:
      checked[index] = True
      for tar in outs[index]:
        memo[index] = max(memo[index], memo_recursion(memo, checked, tar, outs)+1)
    return memo[index]

  ans = 0
  memo = [0]*N
  checked = [False]*N

  for i in topological_graph:
    ans = max(ans, memo_recursion(memo, checked, i, out_))

  # ans = 0
  # dp = [0]*N
  # for i in reversed(topological_graph):
  #   # 葉だったら 0。
  #   if len(out_[i])==0: dp[i]=0
  #   else:
  #     for j in out_[i]:
  #       dp[i] = max(dp[i], dp[j]+1)
  #     ans = max(ans, dp[i])
  print(ans)

resolve()


if __name__ == "__main__":
    unittest.main()
