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
        input = """2
01
10"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
011
101
110"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
010110
101001
010100
101000
100000
010000"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  # BFS して深さ毎に V でくくることを考える。
  # 開始点からある頂点までのの距離が経路によって違う時、
  # 隣りあわない V 間で頂点が結ばれてしまう。
  # 開始点と全ての頂点前での距離が経路によらず一定である時、条件を満たす分割ができる。
  # 開始点によって最大分割数が変わるため、全ての頂点を開始点にして試す。
  N = int(input())
  S = [[int(x) for x in list(input())] for _ in range(N)]
  EDGES = [set() for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if S[i][j]: EDGES[i].add(j)

  nexts = deque()
  ans = -1
  for i in range(N):
    nexts.append(i)
    checked = [False]*N
    checked[i] = True
    distance = [0]*N
    max_d = 0
    used = set()
    while nexts:
      c = nexts.popleft()
      used.add(c)
      if distance[c] > max_d:
        max_d = distance[c]

      for n in EDGES[c]:
        if checked[n]:
          if n in used: continue
          if distance[n] != distance[c]+1:
            break
          continue
        checked[n] = True
        distance[n] = distance[c]+1
        nexts.append(n)
      else:
        continue
      break
    else:
      ans = max(ans, max_d+1)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()