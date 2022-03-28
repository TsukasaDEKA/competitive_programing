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
        input = """3
0 1 3
1 0 2
3 2 0"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
0 1 3
1 0 1
3 1 0"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
0 21 18 11 28
21 0 13 10 26
18 13 0 23 13
11 10 23 0 17
28 26 13 17 0"""
        output = """82"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """3
0 1000000000 1000000000
1000000000 0 1000000000
1000000000 1000000000 0"""
        output = """3000000000"""
        self.assertIO(input, output)

def resolve():
  # N が小さい。
  # 任意の 3 点を選んだ時に、三角形(面積 0 も含む)を作れない場合は -1 を返す。
  # 直接繋がっている街と直接繋がっていない街がある。
  # 直接繋がっている街とそうでない街の判定をどうするかが焦点
  # i から j, k の街までの距離が Aij, Aik なので、
  # Aik - Aij == Ajk の時、j が真ん中になっている。(k と i は直接繋がっていない。)
  # Aij - Aik == Ajk の時、k が真ん中になっている。(i と j は直接繋がっていない。)
  # Aij + Aik == Ajk の時、i が真ん中になっている。(j と k は直接繋がっていない。)
  # 直接繋がっていない点を記録していけばいけそう。
  N = int(input())
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]
  CONNECT = [set(list(range(i+1, N))) for i in range(N)]
  for i in range(N-2):
    for j in range(i+1, N-1):
      Aij = A[i][j]
      for k in range(j+1, N):
        if k not in CONNECT[i]:
          continue
        Ajk, Aki = A[j][k], A[k][i]
        a, b, c = sorted([Aij, Ajk, Aki])
        if a+b < c:
          print(-1)
          return

        if Aki - Aij == Ajk:
          if k in CONNECT[i]:
            CONNECT[i].remove(k)
        if Aij - Aki == Ajk:
          if j in CONNECT[i]:
            CONNECT[i].remove(j)
        if Aij + Aki == Ajk:
          if k in CONNECT[j]:
            CONNECT[j].remove(k)

  ans = 0
  for i in range(N):
    for j in CONNECT[i]:
      ans += A[i][j]
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()