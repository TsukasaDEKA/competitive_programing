from collections import deque
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
        input = """7
b a b a b b a
2 1
3 7
3 2
3 4
5 4
4 6"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
a b
1 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """22
b a b b a b b b a b a a a a b b a b b a a a
1 7
4 14
12 22
2 4
21 17
3 20
7 8
20 14
15 11
8 14
9 12
17 8
6 20
11 20
18 19
10 8
22 20
13 21
5 14
19 20
16 14"""
        output = """16"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  # 余事象?
  # 絶対切っちゃダメなところがあって、2**(切っちゃダメな辺の個数) とかなら楽
  # なんだけど、 2 箇所同時に切って初めてダメになるパターンがあるのでそれだと難しい。
  # a, b のどちらかだけが含まれる区間を決める => その内どこか 2 箇所を切る組み合わせを決める
  # 木 DP ？
  # dp[i] := ノード i 以下の条件を満たす切り方の場合数
  # DFS のバックトラックで処理すると良さそう。
  # 部分木がわかれば、
  mod = 10**9+7
  N = int(input())
  C = [""]+[x for x in input().split(" ")]
  EDGES = [set() for _ in range(N+1)]
  for i in range(N-1):
    a, b = [int(x) for x in input().split(" ")]
    EDGES[a].add(b)
    EDGES[b].add(a)

  dp = [[0]*3 for i in range(N+1)]

  nexts = deque()
  nexts.append((-1, None))
  nexts.append((1, None))
  checked = [False]*(N+1)
  checked[1] = True
  while nexts:
    i, parent = nexts.pop()
    if i < 0:
      i*=-1
      temp = 1
      flag = False
      c = 0 if C[i] == "a" else 1
      for e in EDGES[i]:
        if e == parent: continue
        if flag:
          temp *= dp[e][c]+dp[e][2]
        else:
          temp = dp[e][c]+dp[e][2]
          flag = True

      dp[i][c] = temp
      dp[i][2] -= temp

      temp = 1
      flag = False
      for e in EDGES[i]:
        if e == parent: continue
        t = dp[e][0]+dp[e][1]+2*dp[e][2]
        if flag:
          temp *= t
        else:
          temp = t
          flag = True

      dp[i][2] += temp
      for j in range(3):
        if dp[i][j] >= mod: dp[i][j]%=mod
      continue

    for e in EDGES[i]:
      if checked[e]: continue
      checked[e] = True
      nexts.append((-e, i))
      nexts.append((e, i))
  # print(*dp, sep="\n")
  print(dp[1][2]%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
