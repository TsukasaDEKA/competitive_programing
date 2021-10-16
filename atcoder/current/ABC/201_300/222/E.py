import sys
from io import StringIO
from typing import Tuple
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
        input = """4 5 0
2 3 2 1 4
1 2
2 3
3 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 10 10000
1 2 1 2 1 2 2 1 1 2
1 2
1 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 2 -1
1 10
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10"""
        output = """126"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5 8 -1
1 4 1 4 2 1 3 5
1 2
4 1
3 1
1 5"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  # 各辺を通る回数をそれぞれ集積することができる。
  # 差が K になるようにグルーピングする方法を求めたい。
  from collections import deque, defaultdict

  mod = 998244353
  N, M, K = map(int, input().split(" "))
  A = [int(x)-1 for x in input().split(" ")]
  EDGES = [[] for _ in range(N+1)]
  for _ in range(N-1):
    u, v = [int(x)-1 for x in input().split(" ")]
    EDGES[u].append(v)
    EDGES[v].append(u)

  nexts = deque()
  nexts.append(0)
  depth = [0]*N
  checked = [False]*N
  checked[0] = True
  parents = [0]*N
  while nexts:
    current = nexts.pop()
    for n in EDGES[current]:
      if checked[n]: continue
      checked[n] = True
      parents[n] = current
      depth[n] = depth[current]+1
      nexts.append(n)

  # 辺を通った回数
  sum_ = 0
  count = [0]*N
  for i in range(M-1):
    s, g = A[i], A[i+1]
    if s == g: continue
    if depth[s] > depth[g]: s, g = g, s

    temp = []
    while g != s:
      if depth[g] == depth[s]: temp.append(s); s = parents[s]
      temp.append(g); g = parents[g]

    sum_+=len(temp)
    for i in temp:
      count[i]+=1

  if (sum_+K)%2:
    print(0)
    return

  tar = min((sum_+K)//2, sum_-(sum_+K)//2)
  count = [x for x in count if x != 0]
  # 出現していない辺は自由に塗れるので 2**<出現していない辺の数>
  ans = pow(2, N-1-len(count), mod)
  dp = defaultdict(int)
  dp[0] = 1
  for val in count:
    for k in reversed(range(tar+1-val)):
      if dp[k] !=0: dp[k+val]+=dp[k]
      if dp[k+val] >= mod: dp[k+val]%=mod

  ans *= dp[tar]
  print(ans%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()