from os import sep
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
        input = """5
1 2
2 3
2 4
4 5
4
1 1 1
1 4 10
2 1 100
2 2 1000"""
        output = """11
110
1110
110
100"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7
2 1
2 3
4 2
4 5
6 1
3 7
7
2 2 1
1 3 2
2 2 4
1 6 8
1 3 16
2 4 32
2 1 64"""
        output = """72
8
13
26
58
72
5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """11
2 1
1 3
3 4
5 2
1 6
1 7
5 8
3 9
3 10
11 4
10
2 6 688
1 10 856
1 8 680
1 8 182
2 2 452
2 4 183
2 6 518
1 3 612
2 6 339
2 3 206"""
        output = """1657
1657
2109
1703
1474
1657
3202
1474
1247
2109
2559"""
        self.assertIO(input, output)

def resolve():
  # imos っぽい感じで要所に x の追加・削除イベントを置くことで処理を行える。
  # t = 1 の時を考える。
  # a が b の子だった場合、 a に x を追加する。
  # a が b の親だった場合、 根に x を、b に -x を追加する。
  # t = 2 の時を考える。
  # b が a の子だった場合、 b に x を追加する。
  # b が a の親だった場合、根に x を、 a に -x を追加する。
  # 対称性があるので t = 1 パターンだけ組んで t = 2 の時に a, b を入れ替えるようにしよう。
  from collections import deque

  inf = 10**18+1
  N = int(input())
  A_B = [[int(x)-1 for x in input().split(" ")] for _ in range(N-1)]
  EDGES = [[] for _ in range(N)]
  for a, b in A_B:
    EDGES[a].append(b)
    EDGES[b].append(a)

  # 根を 0 に設定して親子関係を構築する。
  nexts = deque()
  nexts.append(0)
  parents = [-1]*N
  parents[0] = N
  while nexts:
    current = nexts.pop()
    for n in EDGES[current]:
      if parents[n] >= 0: continue
      parents[n] = current
      nexts.append(n)

  imos = [0]*N
  Q = int(input())
  for _ in range(Q):
    t, e, x = [int(x) for x in input().split(" ")]
    e -= 1
    a, b = A_B[e]
    if t == 2:
      a, b = b, a

    if parents[b] == a:
      imos[0] += x
      imos[b] -= x
    else:
      imos[a] += x

  nexts.append(0)
  while nexts:
    current = nexts.pop()
    for n in EDGES[current]:
      if parents[current] == n: continue
      nexts.append(n)
      imos[n]+=imos[current]
  print(*imos, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()