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
        input = """eye lid
4
lie
die
did
dye"""
        output = """3
eye
dye
die
lie
lid"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """eye eye
4
lie
die
did
dye"""
        output = """0
eye
eye"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """eye lid
4
lie
lip
did
dye"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  from collections import deque

  # グラフを作って BFS。
  # グラフ構築に (4*1000)**2 = 16*10**6 必要なのでちょっと厳しいかも？
  first, last = [list(x) for x in input().split(" ")]
  N = int(input())
  S = [first]+[list(input()) for _ in range(N)]+[last]
  N = len(S)

  if first == last:
    print(0, "".join(first), "".join(last), sep="\n")
    return
  # グラフを構築
  EDGES = [[] for _ in range(N+2)]
  for i in range(N-1):
    si = S[i]
    for j in range(i+1, N):
      sj = S[j]
      count = len([1 for x, y in zip(si, sj) if x != y])
      if count == 1:
        EDGES[i].append(j)
        EDGES[j].append(i)

  # BFS
  # 遡れるように親を記録していく。
  parent = [-1]*N
  nexts = deque()
  nexts.append(0)
  checked = [False]*N
  checked[0] = True
  while nexts:
    current = nexts.popleft()
    for n in EDGES[current]:
      if checked[n]: continue
      checked[n] = True
      parent[n] = current
      nexts.append(n)

  # last から遡りながら経路を復元する。
  # 逆順が答え。
  ans_i = []
  i = len(S)-1
  while i >= 0:
    ans_i.append(i)
    i = parent[i]


  # first まで遡れない場合は -1 を出力
  if ans_i[-1] != 0:
    print(-1)
    return
  
  ans = ["".join(S[i]) for i in ans_i[::-1]]
  print(len(ans)-2)
  print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()