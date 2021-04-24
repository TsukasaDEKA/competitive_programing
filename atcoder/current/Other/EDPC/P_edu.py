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
1 2
2 3"""
        output = """5"""
        self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """4
# 1 2
# 1 3
# 1 4"""
#         output = """9"""
#         self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """1"""
#         output = """2"""
#         self.assertIO(input, output)

#     def test_Sample_Input_4(self):
#         input = """10
# 8 5
# 10 8
# 6 5
# 1 5
# 4 8
# 2 10
# 3 6
# 9 2
# 1 7"""
#         output = """157"""
#         self.assertIO(input, output)

def resolve():
  # 「隣り合う頂点どうしをともに黒で塗ってはいけません。」だけど、白はいくつ連続してても OK
  # 木構造
  # DP の問題
  # 白だった場合と黒だった場合を想定して配っていく？
  # 中心点が黒だった場合、他は白一択
  # 中心点が白だった場合、2**n (n はノードの個数) になる。
  # 木 DP なるものがあるらしい。
  from collections import defaultdict, deque

  mod = 10**9+7
  inf = 10**18+1
  N = int(input())
  edge = defaultdict(set)

  for i in range(N-1):
    x, y = [int(x)-1 for x in input().split(" ")]
    edge[x].add(y)
    edge[y].add(x)

  dp = [[0]*2 for _ in range(N)]
  def solve(parent, i):
    if (len(edge[i]) == 1 and list(edge[i])[0] == parent) or len(edge[i]) == 0:
      dp[i][0] = dp[i][1] = 1 
      return

    dp[i]
    for n in edge[i]:
      if n == parent: continue
      dp[i] *= solve(i, n)
    dp[i]+=1
    return dp[i]
  solve(None, 0)
  print(*dp)
# resolve()

if __name__ == "__main__":
    unittest.main()
